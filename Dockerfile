FROM python:3.10-alpine as base
LABEL maintainer="graphenex.project@protonmail.com"
ENV LC_ALL=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1
WORKDIR /app

FROM base as builder
RUN apk update \
    && apk add --no-cache \
    gcc \
    libffi-dev \
    linux-headers \
    musl-dev \
    python3-dev
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN pip install poetry
COPY . .
RUN poetry install --no-ansi

FROM base as runtime
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=builder /app /app
EXPOSE 8080

# https://github.com/grapheneX/grapheneX/issues/127
RUN sed -i '/Mapping/s/collections/collections.abc/' /app/.venv/lib/python3.10/site-packages/prompt_toolkit/styles/from_dict.py

CMD ["/bin/sh", "-c", "grapheneX"]