from sqlalchemy import Column, Integer, String
from .base import Base


class Enums(Base):
    __tablename__ = "enums"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    group = Column(String(32), nullable=False, comment="枚举组别")
    key = Column(Integer, nullable=False, comment="枚举键")
    value = Column(String(32), nullable=False, comment="枚举值")

