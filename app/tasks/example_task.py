import time
from app.tasks.celery_app import celery_app


@celery_app.task
def example_background_task():
    """Örnek bir arkaplan görevi."""
    # Simüle edilmiş işleme süresi
    time.sleep(10)
    return {"status": "completed", "result": "Task completed successfully"}