from pydantic import BaseModel, field_validator
import re

class CreateCustomerRequest(BaseModel):

    first_name: str
    last_name: str
    phone: str

    @field_validator('phone', mode="before")
    def validate_phone_numbers(cls, phone):

        if not re.match(r'^\+?[0-9]{6,15}$', phone):
            raise ValueError(f"Invalid phone number: {phone}. Use a valid international phone number format.")
        
        return phone