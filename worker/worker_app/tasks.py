# worker/worker_app/tasks.py
from celery import Celery
import os

# Initialize Celery app
app = Celery(
    "worker_app",
    broker=os.environ.get("REDIS_URL"),
    backend=os.environ.get("REDIS_URL"),
    include=["worker_app.tasks"],
)

# Configure Celery
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@app.task(bind=True, max_retries=3)
def test_connection(self, worker_id):
    try:
        return f"Worker {worker_id} is connected and working"
    except Exception as exc:
        self.retry(exc=exc, countdown=10)


@app.task(bind=True, max_retries=3)
def get_recommendations(self, user_id):
    try:
        # Mock recommendation logic
        return {
            "user_id": user_id,
            "recommendations": [
                {"movie_id": 1, "score": 0.9},
                {"movie_id": 2, "score": 0.8},
                {"movie_id": 3, "score": 0.7},
            ],
        }
    except Exception as exc:
        self.retry(exc=exc, countdown=10)
