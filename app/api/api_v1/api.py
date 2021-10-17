from fastapi import APIRouter

from .endpoints import business, user, video


router = APIRouter()

router.include_router(business.router, prefix='/business', tags=['business'])
router.include_router(user.router, prefix='/user', tags=['user'])
router.include_router(video.router, prefix='/video', tags=['video'])
