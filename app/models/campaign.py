
from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Campaign(BaseModel):

    __tablename__ = 'campaigns'

    name = Column(String(50), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    calls = relationship("Call", back_populates="campaign")

    def is_active(self):
        return self.start_time <= datetime.now(timezone.utc) <= self.end_time