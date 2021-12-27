from sqlalchemy import Boolean, Column, Integer, String
from .base import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(32), unique=True, index=True, nullable=False)
    hashed_password = Column(String(32), nullable=False)
    is_active = Column(Boolean, default=True)