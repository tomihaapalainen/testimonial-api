from pydantic import BaseModel


class TestimonialRequestBase(BaseModel):
    questions: str

    class Config:
        orm_mode = True


class TestimonialRequest(TestimonialRequestBase):
    id: int
    business_id: int
    created_on: int
