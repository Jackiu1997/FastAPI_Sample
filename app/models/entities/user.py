from sqlalchemy import Boolean, Column, Integer, String
from .base import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(32), unique=True, index=True, nullable=False, comment="用户名")
    hashed_password = Column(String(32), nullable=False, comment="HASH密码")
    is_active = Column(Boolean, default=True, comment="激活状态")