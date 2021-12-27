from typing import Optional
from pydantic import BaseModel


class PublicationRequest(BaseModel):
    title: str
    author: str
    jounal: str
    cover: Optional[str] = None
    date: Optional[str] = None
    link: Optional[str] = None
    show_on_main: bool = True


class PublicationResponse(PublicationRequest):
    id: int

    class Config:
        orm_mode = True