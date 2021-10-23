import time

from typing import Any, Dict

from uuid import uuid4

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models import TestimonialRequest


def create(db: Session, business_id: int):
    public_id = str(uuid4())
    timestamp = round(time.time())
    db_testimonial_request = TestimonialRequest(
        business_id=business_id,
        public_id=public_id,
        created_on=timestamp)
    db.add(db_testimonial_request)
    db.commit()
    db.refresh(db_testimonial_request)
    return db_testimonial_request


def read_by_id(db: Session, testimonial_request_id: int):
    return db.query(TestimonialRequest)\
        .filter(TestimonialRequest.id == testimonial_request_id)\
        .first()


def read_by_public_id(db: Session, public_id: str) -> TestimonialRequest:
    return db.query(TestimonialRequest).filter(TestimonialRequest.public_id == public_id).first()


def update(db: Session, testimonial_request: TestimonialRequest, values: Dict[str, Any]):
    testimonial_request_data = jsonable_encoder(testimonial_request)

    for field in testimonial_request_data:
        if field in values:
            setattr(testimonial_request, field, values[field])

    db.add(testimonial_request)
    db.commit()
    db.refresh(testimonial_request)
    return testimonial_request
