import time

from typing import Any, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models import Business
from app.schemas.business import BusinessIn


def create(db: Session, business_in: BusinessIn):
    timestamp = round(time.time())
    db_business = Business(**dict(business_in), created_on=timestamp)
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business


def read_by_business_identity(db: Session, business_identity: str):
    return db.query(Business).filter(Business.identity == business_identity).first()


def update(db: Session, business: Business, values: Dict[str, Any]):
    user_data = jsonable_encoder(business)

    for field in user_data:
        if field in values:
            setattr(business, field, values[field])

    db.add(business)
    db.commit()
    db.refresh(business)
    return business
