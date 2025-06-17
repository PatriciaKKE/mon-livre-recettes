FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root

COPY . .

EXPOSE 3001
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:3001"]
