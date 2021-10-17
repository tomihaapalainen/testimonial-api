from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.crud import business_crud
from app.db import get_db
from app.firebase.auth import get_current_user_by_token
from app.models import User
from app.schemas.business import BusinessIn, BusinessOut


router = APIRouter()


@router.post('/', response_model=BusinessOut)
async def create_business(business_in: BusinessIn, db: Session = Depends(get_db)):
    try:
        print(dict(business_in))
        db_business = business_crud.create(db, business_in)
        return db_business
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=403,
            detail=f'Unable to create business with business ID {business_in.identity}.')


@router.get('/', response_model=BusinessOut)
async def read_business(
    user: User = Depends(get_current_user_by_token),
):
    return user.business
