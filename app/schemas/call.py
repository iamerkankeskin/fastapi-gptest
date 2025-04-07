from pydantic import BaseModel
from datetime import timedelta
from typing import List

class CallReportRequest(BaseModel):
    phone_number: str
    call_duration: timedelta
    status: str

    class Config:
        orm_mode = True
