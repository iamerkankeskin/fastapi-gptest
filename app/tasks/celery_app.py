from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "worker",
    broker=str(REDIS_URL),
    backend=str(REDIS_URL),
    include=["app.tasks.example_task"]
)

# Celery ayarları
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Istanbul",
    enable_utc=True,
    worker_hijack_root_logger=False,
)