from pydantic import BaseModel, EmailStr

from .business import BusinessOut


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    business_identity: str

    class Config:
        orm_mode = True


class UserIn(UserBase):
    password: str


class User(UserBase):
    id: int
    is_admin: bool


class UserOut(UserBase):
    business: BusinessOut
