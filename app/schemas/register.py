from pydantic import BaseModel, EmailStr


class RegisterBase(BaseModel):
    email: EmailStr
    user_name: str
    business_name: str
    business_identity: str

    class Config:
        orm_mode = True


class RegisterIn(RegisterBase):
    pass


class Register(RegisterBase):
    id: int
    has_premium: bool
    created_on: int


class RegisterOut(RegisterBase):
    created_on: int
