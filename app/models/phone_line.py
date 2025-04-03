from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import String, Boolean
from sqlalchemy.orm import relationship

class PhoneLine(BaseModel):

    __tablename__ = 'phone_lines'
    line_number = Column(String, unique=True)
    status = Column(Boolean, default="available")

    calls = relationship("Call", back_populates="phone_line")