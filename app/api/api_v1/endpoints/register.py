from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.crud import business_crud, user_crud
from app.db import get_db
from app.schemas.business import BusinessIn
from app.schemas.register import RegisterIn, RegisterOut
from app.schemas.user import UserIn


router = APIRouter()


@router.post('/new', response_model=RegisterOut)
async def register(register_in: RegisterIn, db: Session = Depends(get_db)):
    user_in = UserIn(email=register_in.email, name=register_in.user_name)
    business_in = BusinessIn(name=register_in.business_name, identity=register_in.business_identity)
    try:
        db_business = business_crud.create(db, business_in)
        db_user = user_crud.create(db, user_in, db_business.id, is_admin=True)
        return {
            'email': db_user.email,
            'user_name': db_user.name,
            'business_name': db_business.name,
            'business_identity': db_business.identity,
            'created_on': db_user.created_on
        }
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=403,
            detail=f'Unable to create business with ID {register_in.business_identity}.')
