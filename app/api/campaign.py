from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.campaign import Campaign
from app.schemas.campaign import CampaignCreateRequest

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])


@router.post("/", response_model=CampaignCreateRequest)

async def create_campaign(campaign: CampaignCreateRequest, db: Session = Depends(get_db)):
    
    new_campaign = Campaign(
        name=campaign.name,
        start_time=campaign.start_time,
        end_time=campaign.end_time,
    )
    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)
    return new_campaign
