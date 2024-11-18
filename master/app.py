# master/app.py
from flask import Flask, jsonify
from celery import Celery
import os

app = Flask(__name__)
celery = Celery("tasks", broker=os.environ.get("REDIS_URL"))


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "redis_url": os.environ.get("REDIS_URL")})


@app.route("/test-workers")
def test_workers():
    results = []
    for i in range(4):
        result = celery.send_task("tasks.test_connection", args=[i])
        results.append(str(result))
    return jsonify({"status": "tasks_sent", "task_ids": results})


@app.route("/recommend/<user_id>")
def recommend(user_id):
    result = celery.send_task("tasks.get_recommendations", args=[user_id])
    return jsonify({"status": "processing", "task_id": str(result)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
