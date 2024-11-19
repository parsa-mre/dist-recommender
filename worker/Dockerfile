# worker/Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the worker package
COPY worker_app ./worker_app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    CELERY_WORKERS=2 \
    CELERY_MAX_TASKS_PER_CHILD=100 \
    CELERY_TASK_TIME_LIMIT=3600 \
    CELERY_TASK_SOFT_TIME_LIMIT=3540

# Start Celery worker
CMD ["celery", "-A", "worker_app.tasks", "worker", \
    "--loglevel=INFO", \
    "--concurrency=${CELERY_WORKERS}", \
    "--max-tasks-per-child=${CELERY_MAX_TASKS_PER_CHILD}", \
    "--time-limit=${CELERY_TASK_TIME_LIMIT}", \
    "--soft-time-limit=${CELERY_TASK_SOFT_TIME_LIMIT}"]