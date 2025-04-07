from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime
from app.schemas.customer import CreateCustomerRequest

class CampaignCreateRequest(BaseModel):
    name: str
    start_time: str
    end_time: str
    customer_ids: List[int]

    @field_validator('start_time', 'end_time', mode='before')
    def parse_times(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return value
    
    @field_validator('customer_ids', mode='before')
    def validate_customer_ids(cls, ids):
        if not isinstance(ids, list):
            raise ValueError("Customer IDs must be provided as a list")
        
        for id in ids:
            if not isinstance(id, int) or id <= 0:
                raise ValueError(f"Invalid customer ID: {id}. Must be a positive integer.")
        
        return ids
    
    model_config = {
        "json_encoders": {
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
    }