from pydantic import BaseModel
from datetime import datetime

class NewsRequest(BaseModel):
    title: str
    abstract: str
    content: str
    show_on_main: bool = True
    

class NewsResponse(NewsRequest):
    id: str
    create_time: datetime

    class Config:
        orm_mode = True