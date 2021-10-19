import time

from typing import Any, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models import TestimonialRequest


def create(db: Session, questions: dict, business_id: int):
    timestamp = round(time.time())
    db_testimonial_request = TestimonialRequest(
        questions=questions,
        business_id=business_id,
        created_on=timestamp)
    db.add(db_testimonial_request)
    db.commit()
    db.refresh(db_testimonial_request)
    return db_testimonial_request


def read_by_id(db: Session, testimonial_request_id: int):
    return db.query(TestimonialRequest)\
        .filter(TestimonialRequest.id == testimonial_request_id)\
        .first()


def update(db: Session, testimonial_request: TestimonialRequest, values: Dict[str, Any]):
    testimonial_request_data = jsonable_encoder(testimonial_request)

    for field in testimonial_request_data:
        if field in values:
            setattr(testimonial_request, field, values[field])

    db.add(testimonial_request)
    db.commit()
    db.refresh(testimonial_request)
    return testimonial_request
