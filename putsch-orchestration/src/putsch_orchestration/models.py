"""Declarative per-agent model routing through LiteLLM.

The architectural contract:
    Swapping the model for any agent is a one-line config change. No agent
    in this codebase imports a provider SDK or hardcodes a model name. The
    binding is a string, resolved at agent-construction time against
    `config.Settings.models`.

Default bindings (defined in config.ModelBinding):
    reasoning              mistral/mistral-large-2     manager, match, supervisor
    german_extraction      huggingface/Qwen2.5-72B     OCR-Agent, intake parsing
    sap_rfc_generation     huggingface/Qwen2.5-Coder   RFC composition (rare)
    german_prose           mistral/mistral-medium-3.5  Buchungs-Agent commentary

Frankfurt-hosted, Mistral La Plateforme is the only external API allowed
under the Putsch network policy. Qwen models run on the on-prem HF
inference endpoint behind the LiteLLM proxy. Both are addressed identically
from this module — the only file that knows which is which is the proxy.
"""

from __future__ import annotations

import enum
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

import litellm
from litellm.utils import get_max_tokens

from putsch_orchestration.config import Settings, get_settings
from putsch_orchestration.logging_setup import get_logger

_log = get_logger(__name__)


class AgentRole(str, enum.Enum):
    """Stable identifiers for every agent role in the system.

    Adding a role is an ADR-level change — the model binding for it must
    be configured before the role is used in production.
    """

    EINGANGS_AGENT = "eingangs_agent"
    OCR_AGENT = "ocr_agent"
    MATCH_AGENT = "match_agent"
    BUCHUNGS_AGENT = "buchungs_agent"
    MANAGER_AGENT = "manager_agent"
    SUPERVISOR = "supervisor"


# Static mapping: which binding key serves which role. Changing this map
# is an ADR-level change; changing the binding *value* (which model the
# key resolves to) is a one-line env change.
_ROLE_TO_BINDING: Mapping[AgentRole, str] = {
    AgentRole.EINGANGS_AGENT: "german_extraction",
    AgentRole.OCR_AGENT: "german_extraction",
    AgentRole.MATCH_AGENT: "reasoning",
    AgentRole.BUCHUNGS_AGENT: "german_prose",
    AgentRole.MANAGER_AGENT: "reasoning",
    AgentRole.SUPERVISOR: "reasoning",
}


@dataclass(frozen=True)
class ModelHandle:
    """A resolved (role -> LiteLLM identifier) pair plus the call kwargs
    that any agent/DSPy module needs to invoke it.

    Carries the LiteLLM `model` string, the proxy `api_base`, and the
    `api_key`. Pass it straight to `litellm.acompletion(**handle.as_kwargs())`
    or hand it to a CrewAI Agent via `llm=handle.to_litellm_router_model()`.
    """

    role: AgentRole
    model: str
    api_base: str
    api_key: str
    max_tokens_hint: int | None = None

    def as_kwargs(self) -> dict[str, Any]:
        kw: dict[str, Any] = {
            "model": self.model,
            "api_base": self.api_base,
            "api_key": self.api_key,
        }
        if self.max_tokens_hint is not None:
            kw["max_tokens"] = self.max_tokens_hint
        return kw


def resolve_model(role: AgentRole, settings: Settings | None = None) -> ModelHandle:
    """Resolve a role to a concrete ModelHandle.

    Cheap (no I/O). Call at agent construction; cache the result on the
    agent if construction is on a hot path.
    """
    s = settings or get_settings()
    binding_key = _ROLE_TO_BINDING[role]
    model_str = getattr(s.models, binding_key)

    try:
        max_tok = get_max_tokens(model_str)
    except Exception:  # litellm raises a variety of errors here
        max_tok = None

    handle = ModelHandle(
        role=role,
        model=model_str,
        api_base=str(s.litellm_base_url),
        api_key=s.litellm_api_key.get_secret_value(),
        max_tokens_hint=max_tok,
    )
    _log.info(
        "model.resolved",
        role=role.value,
        binding=binding_key,
        model=model_str,
    )
    return handle


async def acomplete(
    handle: ModelHandle,
    messages: list[dict[str, str]],
    **kwargs: Any,
) -> Any:
    """Thin async wrapper over litellm.acompletion.

    Why wrap: every model call in this codebase goes through one function so
    we can attach a tracer span, redact prompts, and pin retry policy in a
    single place when the observability module ships.
    """
    call_kwargs = handle.as_kwargs() | kwargs
    return await litellm.acompletion(messages=messages, **call_kwargs)


__all__ = [
    "AgentRole",
    "ModelHandle",
    "acomplete",
    "resolve_model",
]
