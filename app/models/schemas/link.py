from typing import Optional
from pydantic import BaseModel


class LinkRequest(BaseModel):
    title: str
    content: Optional[str] = None
    image: Optional[str] = None
    url: str
    category: int = 0


class LinkResponse(LinkRequest):
    id: int

    class Config:
        orm_mode = True