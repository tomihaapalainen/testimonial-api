from fastapi import APIRouter

from .endpoints import (
    business,
    register,
    testimonial,
    testimonialrequest,
    user,
    video)


router = APIRouter()

router.include_router(business.router, prefix='/business', tags=['business'])
router.include_router(register.router, prefix='/register', tags=['register'])
router.include_router(testimonial.router, prefix='/testimonial', tags=['testimonial'])
router.include_router(
    testimonialrequest.router, prefix='/testimonialrequest', tags=['testimonialrequest'])
router.include_router(user.router, prefix='/user', tags=['user'])
router.include_router(video.router, prefix='/video', tags=['video'])
