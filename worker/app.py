# worker/tasks.py
from celery import Celery
import os

app = Celery("tasks", broker=os.environ.get("REDIS_URL"))


@app.task
def test_connection(worker_id):
    return f"Worker {worker_id} is connected and working"


@app.task
def get_recommendations(user_id):
    # Mock recommendation logic
    # In reality, this would query the external DB and process data
    return {
        "user_id": user_id,
        "recommendations": [
            {"movie_id": 1, "score": 0.9},
            {"movie_id": 2, "score": 0.8},
            {"movie_id": 3, "score": 0.7},
        ],
    }
