from fastapi import APIRouter

from .endpoints import video


router = APIRouter()

router.include_router(video.router, prefix='/video', tags=['users'])
