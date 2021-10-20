from pydantic import BaseModel


class TestimonialRequest(BaseModel):
    id: int
    business_id: int
    public_id: str
    created_on: int

    class Config:
        orm_mode = True


class TestimonialRequestOut(BaseModel):
    public_id: str
    business_name: str

    class Config:
        orm_mode = True
