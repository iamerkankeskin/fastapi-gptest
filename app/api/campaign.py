from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.campaign import Campaign, CampaignCustomer
from app.schemas.campaign import CampaignCreateRequest

router = APIRouter(prefix="/campaign", tags=["Campaigns"])

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

    # create relations between campaign & customer
    for customer_id in campaign.customer_ids:
        campaign_customer = CampaignCustomer(
            campaign_id=new_campaign.id,
            customer_id=customer_id
        )
        db.add(campaign_customer)
    
    db.commit()
    db.refresh(campaign_customer)

    return new_campaign
