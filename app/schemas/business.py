from typing import List

from pydantic import BaseModel

from .testimonial import TestimonialOut
from .user import UserOut


class BusinessBase(BaseModel):
    name: str
    identity: str

    class Config:
        orm_mode = True


class BusinessIn(BusinessBase):
    pass


class Business(BusinessBase):
    id: int
    has_premium: bool
    created_on: int

    users: List[UserOut]
    testimonials = List[TestimonialOut]


class BusinessOut(BusinessBase):
    pass
