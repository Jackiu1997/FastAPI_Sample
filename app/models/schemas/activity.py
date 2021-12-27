from typing import Optional
from pydantic import BaseModel


class ActivityRequest(BaseModel):
    title: str
    content: Optional[str] = None
    date: Optional[str] = None
    image: str


class ActivityResponse(ActivityRequest):
    id: int

    class Config:
        orm_mode = True