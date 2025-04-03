from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Recording(BaseModel):

    __tablename__ = "recordings"
    
    call_id = Column(Integer, ForeignKey("calls.id"))
    duration = Column(Integer)
    
    call = relationship("Call", back_populates="recording")
