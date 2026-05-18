FROM python:3.11-slim-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_ROOT_USER_ACTION=ignore

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        libpq5 \
        tini \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --uid 10001 --shell /bin/false putsch
WORKDIR /app

# --- build stage: install deps into a venv ---
FROM base AS build
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

COPY pyproject.toml /app/
COPY src /app/src
RUN pip install --upgrade pip wheel \
    && pip install --no-cache-dir /app

# --- runtime stage ---
FROM base AS runtime
COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

COPY --chown=putsch:putsch src /app/src
COPY --chown=putsch:putsch pyproject.toml /app/

USER putsch
ENTRYPOINT ["tini", "--", "python", "-m", "putsch_orchestration"]
CMD ["serve"]

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import putsch_orchestration; print('ok')" || exit 1
