from time import sleep
from datetime import datetime
from app.models.call import Call, CallStatus
from app.db.session import SessionLocal
from app.tasks import celery_app
from app.models.phone_line import PhoneLine

@celery_app.task
def simulate_call(call_id: int):
    db = SessionLocal()
    try:
        call = db.query(Call).filter(Call.id == call_id).first()
        if not call:
            return f"Call ID {call_id} not found."
        
        phone_line = db.query(PhoneLine).filter(PhoneLine.is_available == True).first()

        if not phone_line:
            call.status = CallStatus.BUSY
            db.commit()
            db.refresh(call)
            return f"No available phone lines. Call ID {call_id} set to busy."

        phone_line.is_available = False
        db.commit()
        
        sleep(30)

        call.end_time = datetime.now()
        call.status = CallStatus.ANSWERED
        call.call_time = datetime.now()

        phone_line.is_available = True

        call.customer.last_call_time = call.call_time

        db.commit()

        db.refresh(call)
        return f"Call ID {call_id} processed with status {call.status}"
    finally:
        db.close()

