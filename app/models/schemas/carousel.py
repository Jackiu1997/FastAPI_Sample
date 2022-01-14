from typing import Optional
from pydantic import BaseModel


class CarouselRequest(BaseModel):
    image: str


class CarouselResponse(CarouselRequest):
    id: int

    class Config:
        orm_mode = True