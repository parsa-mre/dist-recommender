#!/bin/bash

cd worker_app
# Start Celery worker
celery -A tasks worker \
    --loglevel=INFO \
    --concurrency="${CELERY_WORKERS}" \
    --max-tasks-per-child="${CELERY_MAX_TASKS_PER_CHILD}" \
    --time-limit="${CELERY_TASK_TIME_LIMIT}" \
    --soft-time-limit="${CELERY_TASK_SOFT_TIME_LIMIT}"
