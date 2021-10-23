from pydantic import BaseModel


class BusinessBase(BaseModel):
    name: str
    identity: str

    class Config:
        orm_mode = True


class BusinessIn(BusinessBase):
    pass


class Business(BusinessBase):
    id: int
    created_on: int


class BusinessOut(BusinessBase):
    created_on: int
