from typing import List

from pydantic import BaseModel

from .testimonial import TestimonialOut


class ClientBase(BaseModel):
    name: str
    identity: str

    class Config:
        orm_mode: True


class ClientIn(ClientBase):
    pass


class Client(ClientBase):
    id: int


class ClientOut(ClientBase):
    testimonials: List[TestimonialOut]
    pass
