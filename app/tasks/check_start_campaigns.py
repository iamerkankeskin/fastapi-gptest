from sqlalchemy.orm import selectinload
from app.models.campaign import Campaign, CampaignCustomer
from app.models.call import Call, CallStatus
from app.db.session import SessionLocal
from app.tasks import celery_app
from app.tasks.simulate_call import simulate_call
from datetime import datetime, timezone

@celery_app.task
def check_and_start_campaigns():
    db = SessionLocal()
    now = datetime.now(timezone.utc)

    try:
        campaigns = db.query(Campaign).filter(
            Campaign.start_time <= now,
            Campaign.end_time >= now,
            Campaign.processed == False
        ).all()

        for campaign in campaigns:
            campaign.processed = True
            db.commit()

            try:
                campaign_customers = db.query(CampaignCustomer).options(
                    selectinload(CampaignCustomer.customer)
                ).filter(
                    CampaignCustomer.campaign_id == campaign.id
                ).all()

                calls_to_add: list = []

                for campaign_customer in campaign_customers:
                    call = Call(
                        customer_id=campaign_customer.customer_id,
                        campaign_id=campaign.id,
                        status=CallStatus.QUEUED
                    )
                    calls_to_add.append(call)

                db.add_all(calls_to_add)
                db.commit()

                for call in calls_to_add:
                    simulate_call.apply_async(args=[call.id])

                campaign.processed = False
                db.commit()

            except Exception as e:
                campaign.processed = False
                db.commit()
                raise e

        return f"{len(campaigns)} campaign checked."

    finally:
        db.close()
