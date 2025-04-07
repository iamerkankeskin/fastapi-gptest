from time import sleep
from datetime import datetime
from app.models.call import Call, CallStatus
from app.db.session import SessionLocal
from app.tasks import celery_app
from app.models.customer import Customer

@celery_app.task
def simulate_call(call_id: int):
    db = SessionLocal()
    try:
        call = db.query(Call).filter(Call.id == call_id).first()
        if not call:
            return f"Call ID {call_id} not found."
        
        sleep(30)

        call.status = CallStatus.ANSWERED
        call.call_time = datetime.now()

        db.commit()
        db.refresh(call)
        return f"Call ID {call_id} processed with status {call.status}"
    finally:
        db.close()

