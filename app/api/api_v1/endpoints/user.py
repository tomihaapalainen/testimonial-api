from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.crud import user_crud
from app.db import get_db
from app.firebase.auth import get_current_user_by_token
from app.models import User
from app.schemas.user import UserIn, UserOut


router = APIRouter()


@router.post('/', response_model=UserOut)
async def create_user(user_in: UserIn, db: Session = Depends(get_db)):
    try:
        db_user = user_crud.create(db, user_in)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=403,
            detail=f'Unable to create user with email {user_in.email}.')


@router.get('/', response_model=UserOut)
async def read_user(
    user: User = Depends(get_current_user_by_token)
):
    return dict(user);