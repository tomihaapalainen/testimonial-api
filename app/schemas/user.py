from pydantic import BaseModel, EmailStr

from .business import BusinessOut


class UserBase(BaseModel):
    email: EmailStr
    name: str
    business_identity: str

    class Config:
        orm_mode = True


class UserIn(UserBase):
    pass


class User(UserBase):
    id: int
    is_admin: bool
    created_on: int


class UserOut(UserBase):
    created_on: int

    business: BusinessOut
