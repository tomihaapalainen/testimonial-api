from typing import List

from pydantic import BaseModel

from .client import ClientOut
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
    is_subscribed: bool
    created_on: int

    users: List[UserOut]
    clients: List[ClientOut]


class BusinessOut(BusinessBase):
    pass
