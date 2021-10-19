from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.crud import testimonialrequest_crud
from app.db import get_db
from app.firebase.auth import get_current_user_by_token
from app.models import TestimonialRequest, User


router = APIRouter()


@router.post('/add')
async def create_testimonial_request(
    request: Request,
    db: Session = Depends(get_db),
    # user: User = Depends(get_current_user_by_token)
):
    questions = await request.json()

    try:
        db_testimonial_request: TestimonialRequest = testimonialrequest_crud.create(db, questions, 1)
        return db_testimonial_request.questions
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=403,
            detail=f'Unable to create testimonial request.')
