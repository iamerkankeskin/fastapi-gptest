from pydantic import BaseModel
from typing import List


class CampaignCreateRequest(BaseModel):
    name: str
    start_time: str
    end_time: str
    target_numbers: List[str]