from fastapi import APIRouter, Depends

from app.firebase.auth import get_current_user_by_token
from app.models import User
from app.schemas.business import BusinessOut


router = APIRouter()


@router.get('/', response_model=BusinessOut)
async def read_business(
    user: User = Depends(get_current_user_by_token),
):
    return user.business
