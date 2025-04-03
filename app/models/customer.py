from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import String, DateTime
from datetime import datetime, timezone

class Customer(BaseModel):

    __tablename__ = 'customers'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    last_call_time = Column(DateTime, default=datetime.now(timezone.utc))