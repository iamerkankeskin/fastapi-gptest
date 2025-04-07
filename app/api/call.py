from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.call import CallReportRequest
from app.models.call import Call
from datetime import datetime
from typing import List

router = APIRouter(prefix="/call", tags=["Calls"])

@router.get("/report", response_model=List[CallReportRequest])
async def call_report(db: Session = Depends(get_db)) -> CallReportRequest:

    calls = db.query(Call).all()

    report: list = []
    for call in calls:
        if call.end_time:
            call_duration = call.end_time - call.call_time
        else:
            call_duration = datetime.now() - call.call_time

        report.append(CallReportRequest(
            phone_number=call.customer.phone,
            call_duration=call_duration,
            status=call.status
        ))

    return report