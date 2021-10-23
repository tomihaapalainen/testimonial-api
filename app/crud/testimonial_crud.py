import time

from typing import Any, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models import Testimonial
from app.schemas.testimonial import TestimonialIn


def create(db: Session, testimonial_in: TestimonialIn, business_id: int):
    timestamp = round(time.time())
    db_testimonial = Testimonial(
        **testimonial_in.dict(exclude={'business_identity'}),
        business_id=business_id,
        is_accepted=False,
        created_on=timestamp)
    db.add(db_testimonial)
    db.commit()
    db.refresh(db_testimonial)
    return db_testimonial


def update(db: Session, testimonial: Testimonial, values: Dict[str, Any]):
    user_data = jsonable_encoder(testimonial)

    for field in user_data:
        if field in values:
            setattr(testimonial, field, values[field])

    db.add(testimonial)
    db.commit()
    db.refresh(testimonial)
    return testimonial
