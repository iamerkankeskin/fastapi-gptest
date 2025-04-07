from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.customer import CreateCustomerRequest
from app.models.customer import Customer
from fastapi import HTTPException, status

router = APIRouter(prefix="/customer", tags=["Campaigns"])

@router.post("/", response_model=CreateCustomerRequest)
async def create_customer(customer: CreateCustomerRequest, db: Session = Depends(get_db)):

    customer_exists = db.query(Customer).filter(Customer.phone == customer.phone).first()

    if customer_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Customer with this phone already exists.",
        )
    
    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        phone=customer.phone,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer
