
# Pull base image
FROM python:3.8.5
# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.5


# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Set work directory
COPY poetry.lock pyproject.toml /code/
WORKDIR /code
# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

# Creating folders, and files for a project:
COPY . /code
