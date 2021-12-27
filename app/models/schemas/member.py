from typing import Optional
from pydantic import BaseModel


class MemberRequest(BaseModel):
    name: str
    avatar: Optional[str] = None
    education: str
    graduated: str
    research_background: Optional[str] = None
    email: str
    telephone: Optional[str] = None
    address: Optional[str] = None
    tutor: Optional[str] = None
    category: int = 0


class MemberResponse(MemberRequest):
    id: int

    class Config:
        orm_mode = True