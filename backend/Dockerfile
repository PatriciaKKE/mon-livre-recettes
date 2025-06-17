
FROM python:3.11-slim

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    PATH="$POETRY_HOME/bin:$PATH"

RUN pip install poetry

ENV PATH="$POETRY_HOME/bin:$PATH"
WORKDIR /app


COPY backend/pyproject.toml backend/poetry.lock* ./


RUN poetry install --no-root


COPY backend/ .


EXPOSE 8000


CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
