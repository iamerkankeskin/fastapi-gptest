from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import String, Boolean

class PhoneLine(BaseModel):

    __tablename__ = 'phone_lines'

    phone = Column(String(20), unique=True, nullable=False)
    is_available = Column(Boolean, default=True)
