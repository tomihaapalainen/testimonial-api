from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.crud import testimonialrequest_crud
from app.db import get_db
from app.schemas.testimonial_request import TestimonialRequestOut


router = APIRouter()


@router.get('/{request_id}', response_model=TestimonialRequestOut)
async def read_testimonial_request(request_id: str, db: Session = Depends(get_db)):
    db_testimonial_request = testimonialrequest_crud.read_by_public_id(db, request_id)
    return {
        'public_id': db_testimonial_request.public_id,
        'business_name': db_testimonial_request.business.name
    }
