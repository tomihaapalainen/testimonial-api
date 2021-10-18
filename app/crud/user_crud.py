import time

from typing import Any, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models import User
from app.schemas.user import UserIn


def create(db: Session, user_in: UserIn, business_id: int, is_admin: bool = False):
    timestamp = round(time.time())
    db_user = User(
        **user_in.dict(),
        business_id=business_id,
        is_admin=is_admin,
        created_on=timestamp)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def update(db: Session, user: User, values: Dict[str, Any]):
    user_data = jsonable_encoder(user)

    for field in user_data:
        if field in values:
            setattr(user, field, values[field])

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
