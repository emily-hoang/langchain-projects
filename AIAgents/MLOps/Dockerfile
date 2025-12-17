# Use official Python slim image
FROM python:3.11-slim

# Do not write .pyc files and ensure stdout/stderr are not buffered
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install common build dependencies required by many ML packages
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  gcc \
  git \
  wget \
  ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Copy requirement file and install Python dependencies
# Make sure you have a requirements.txt at the project root
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip \
  && pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY . /app

# Create a non-root user to run the training process
RUN useradd --create-home --shell /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Default command to run training script; override when running container if needed
# Ensure your training entrypoint is named train.py or change this CMD accordingly
CMD ["python", "train.py"]