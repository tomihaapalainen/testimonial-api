import shutil
import time

from typing import List

from fastapi import APIRouter, Depends, File, HTTPException, Response, UploadFile

from sqlalchemy.orm import Session

from app.crud import business_crud, testimonial_crud
from app.db import get_db
from app.firebase.auth import get_current_user_by_token
from app.models import User
from app.schemas.testimonial import TestimonialIn, TestimonialOut, TestimonialUpdate


router = APIRouter()


@router.post('/new')
async def create_testimonial(
    testimonial_in: TestimonialIn,
    db: Session = Depends(get_db)
):
    db_business = business_crud.read_by_business_identity(db, testimonial_in.business_identity)
    testimonial_crud.create(db, testimonial_in, db_business.id)
    return Response(status_code=201)


@router.post('/image')
async def create_image(image: UploadFile = File(...)):
    timestamp = str(time.time()).replace('.', '')
    # TODO: real implementation
    url = f'{timestamp}.png'
    with open(url, 'wb') as f:
        shutil.copyfileobj(image.file, f)
    return {
        'url': url
    }


@router.post('/video')
async def create_video(video: UploadFile = File(...)):
    timestamp = str(time.time()).replace('.', '')
    # TODO: real implementation
    url = f'{timestamp}.webm'
    with open(url, 'wb') as f:
        shutil.copyfileobj(video.file, f)
    return {
        'url': url
    }


@router.get('/all', response_model=List[TestimonialOut])
async def read_all_testimonials(user: User = Depends(get_current_user_by_token)):
    return user.business.testimonials


@router.post('/update', response_model=TestimonialOut)
async def update_testimonial(
    testimonial_update: TestimonialUpdate,
    user: User = Depends(get_current_user_by_token),
    db: Session = Depends(get_db)
):
    try:
        db_testimonial = testimonial_crud.read_by_id(db, testimonial_update.id)
        assert db_testimonial.business_id == user.business_id
        return testimonial_crud.update(
            db, db_testimonial, testimonial_update.dict(exclude={'id'}))
    except AssertionError:
        raise HTTPException(
            status_code=403,
            detail='You do not have permission to update the requested testimonial')
