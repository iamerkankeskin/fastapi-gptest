
from app.models.base import BaseModel
from sqlalchemy import Column
from sqlalchemy import String, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Campaign(BaseModel):

    __tablename__ = 'campaigns'

    name = Column(String(50), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    # relationship
    customers = relationship("CampaignCustomer", back_populates="campaign")
    calls = relationship("Call", back_populates="campaign")

    processed = Column(Boolean, default=False)

    def is_active(self):
        return self.start_time <= datetime.now(timezone.utc) <= self.end_time
    
class CampaignCustomer(BaseModel):
    __tablename__ = 'campaign_customers'
    
    campaign_id = Column(Integer, ForeignKey('campaigns.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # relationship    
    campaign = relationship("Campaign", back_populates="customers")
    customer = relationship("Customer", back_populates="campaigns")