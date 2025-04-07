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
    phone_line_id = Column(Integer, ForeignKey("phone_lines.id"), index=True)
    call_time = Column(DateTime, default=datetime.now(timezone.utc))
    status = Column(Enum(CallStatus), nullable=False, default=CallStatus.ANSWERED)
    end_time = Column(DateTime, nullable=True)
    
    customer = relationship("Customer", back_populates="calls")
    campaign = relationship("Campaign", back_populates="calls")
    phone_line = relationship("PhoneLine", back_populates="phone_lines")