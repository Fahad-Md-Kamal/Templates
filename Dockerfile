# Use an official Python runtime as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy the pyproject.toml and poetry.lock files into the container at /app
COPY pyproject.toml poetry.lock /app/

# Install project dependencies using poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the application code into the container at /app
COPY . /app/
