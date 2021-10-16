from typing import Optional

from pydantic import BaseModel


class TestimonialBase(BaseModel):
    name: str
    title: Optional[str]
    business_name: Optional[str]
    picture_url = Optional[str]

    text: Optional[str]
    audio_url: Optional[str]
    video_url: Optional[str]

    class Config:
        orm_mode = True


class TestimonialIn(TestimonialBase):
    pass


class Testimonial(TestimonialBase):
    id: int
    business_id: int
    client_id: int
    is_accepted: bool


class TestimonialOut(TestimonialBase):
    is_accepted: bool
