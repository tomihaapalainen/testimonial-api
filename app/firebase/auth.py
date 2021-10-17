from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth
from sqlalchemy.orm import Session

from app.crud import user_crud
from app.db import get_db
from app.firebase.admin import firebase_app
from app.schemas.user import UserIn


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


async def get_user_by_username(db: Session, username: str):
    db_user = user_crud.read_by_email(db, username)
    return db_user


async def get_current_user_by_token(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        data = auth.verify_id_token(token, app=firebase_app, check_revoked=True)
        username = data['email']
        user = await get_user_by_username(db, username=username)
        return user
    except (auth.auth.ExpiredIdTokenError, auth.auth.RevokedIdTokenError):
        raise HTTPException(
            status_code=401,
            detail='ID token is expired or has been revoked. Please sign in again.',
            headers={'WWW-Authenticate': 'Bearer'})
    except (auth.InvalidIdTokenError, ValueError):
        raise HTTPException(
            status_code=401,
            detail='Invalid ID token. Please sign in again.',
            headers={'WWW-Authenticate': 'Bearer'})
