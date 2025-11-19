FROM python:alpine
WORKDIR /app
RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root
COPY . .
CMD ["pytest", "-v", "tests/test_device.py"]