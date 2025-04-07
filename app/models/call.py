from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.models.base import BaseModel
from enum import Enum as PyEnum

class CallStatus(str, PyEnum):
    ANSWERED = "answered"
    CANCELED = "canceled"
    BUSY = "busy"
    QUEUED = "queued"

class Call(BaseModel):

    __tablename__ = "calls"
    
    customer_id = Column(Integer, ForeignKey("customers.id"), index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), index=True)
    call_time = Column(DateTime, default=datetime.now(timezone.utc))
    status = Column(Enum(CallStatus), nullable=False, default=CallStatus.ANSWERED)
    
    customer = relationship("Customer", back_populates="calls")
    campaign = relationship("Campaign", back_populates="calls")
    
    recording = relationship("Recording", uselist=False, back_populates="call")