from typing import Optional

from pydantic import BaseModel


class TestimonialBase(BaseModel):
    giver_name: str
    giver_title: str
    business_name: Optional[str] = None
    picture_url: Optional[str] = None

    text: Optional[str] = None
    video_url: Optional[str] = None

    class Config:
        orm_mode = True


class TestimonialIn(TestimonialBase):
    business_identity: str


class Testimonial(TestimonialBase):
    id: int
    business_id: int
    is_accepted: bool
    created_on: int


class TestimonialOut(TestimonialBase):
    id: int
    is_accepted: bool
    created_on: int


class TestimonialUpdate(BaseModel):
    id: int
    is_accepted: bool
