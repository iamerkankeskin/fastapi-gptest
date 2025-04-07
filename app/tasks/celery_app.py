from celery import Celery
from dotenv import load_dotenv
import os


load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "worker",
    broker=str(REDIS_URL),
    backend=str(REDIS_URL)
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Europe/Istanbul",
    enable_utc=True,
    worker_hijack_root_logger=False,
)

beat_schedule={
    'check-and-start-campaigns': {
        'task': 'app.tasks.check_start_campaigns',
        'schedule': 30.0,
    },
}