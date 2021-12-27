from pydantic import BaseModel


class InterestRequest(BaseModel):
    title: str
    content: str
    image: str


class InterestResponse(InterestRequest):
    id: int

    class Config:
        orm_mode = True