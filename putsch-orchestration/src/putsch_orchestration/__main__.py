"""CLI entrypoint for the orchestration service.

Two subcommands:
    run-once     Drain one invoice through the graph from the command line.
                 Useful in CI for the integration tests and as a smoke check.
    serve        Stub for the future FastAPI workflow API. Today it just
                 prints the resolved config and exits 0 so deployment
                 pipelines can validate the container before the API ships.

Real production traffic enters via the workflow API once that module is
built; this CLI is the seam for local dev and chaos tests.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from typing import Any

from putsch_orchestration.config import get_settings
from putsch_orchestration.graph import compiled_graph
from putsch_orchestration.logging_setup import configure_logging, get_logger, set_correlation_id
from putsch_orchestration.obs_hooks import configure_tracing
from putsch_orchestration.sanitize import TaintedText
from putsch_orchestration.state import IntakeChannel, InvoiceState, new_correlation_id

_log = get_logger(__name__)


async def _run_once(args: argparse.Namespace) -> int:
    settings = get_settings()
    raw_text = (
        TaintedText(value=args.raw_text, source="ocr") if args.raw_text else None
    )
    state = InvoiceState(
        thread_id=args.thread_id or new_correlation_id(),
        intake_channel=IntakeChannel(args.intake_channel),
        source_uri=args.source_uri,
        raw_text=raw_text,
    )
    set_correlation_id(state.correlation_id)

    async with compiled_graph(settings) as compiled:
        config: dict[str, Any] = {"configurable": {"thread_id": state.thread_id}}
        result = await compiled.app.ainvoke(state, config=config)
        sys.stdout.write(json.dumps({"final_state": result}, default=str, indent=2))
        sys.stdout.write("\n")
    return 0


def _serve(_: argparse.Namespace) -> int:
    settings = get_settings()
    _log.info(
        "serve.ready_stub",
        environment=settings.environment.value,
        service=settings.service_name,
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    configure_logging()
    configure_tracing()

    parser = argparse.ArgumentParser(prog="putsch-orchestration")
    sub = parser.add_subparsers(dest="cmd", required=True)

    one = sub.add_parser("run-once", help="Drain one invoice through the graph.")
    one.add_argument("--source-uri", required=True)
    one.add_argument("--intake-channel", default="email", choices=[c.value for c in IntakeChannel])
    one.add_argument("--raw-text", default=None)
    one.add_argument("--thread-id", default=None)

    sub.add_parser("serve", help="Print resolved config and exit 0.")

    args = parser.parse_args(argv)
    if args.cmd == "run-once":
        return asyncio.run(_run_once(args))
    if args.cmd == "serve":
        return _serve(args)
    parser.print_help(sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
