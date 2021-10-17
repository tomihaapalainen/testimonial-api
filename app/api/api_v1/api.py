from fastapi import APIRouter

from .endpoints import user, video


router = APIRouter()

router.include_router(user.router, prefix='/user', tags=['user'])
router.include_router(video.router, prefix='/video', tags=['video'])
