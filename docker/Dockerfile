FROM python:3.10-slim as python
LABEL maintainer="graphenex.project@protonmail.com"
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=true
WORKDIR /app

FROM python as poetry
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN poetry install --no-interaction --no-ansi -vvv

FROM python as runtime
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=poetry /app /app
EXPOSE 8080

RUN sed -i '/Mapping/s/collections/collections.abc/' /app/.venv/lib/python3.10/site-packages/prompt_toolkit/styles/from_dict.py

CMD ["/bin/sh", "-c", "grapheneX"]