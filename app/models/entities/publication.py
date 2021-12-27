from datetime import date
from sqlalchemy import Column, Integer, String, Text, Boolean
from .base import Base


class Publications(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=False)
    author = Column(Text)
    jounal = Column(Text)
    cover = Column(Text)
    date = Column(String(32))
    link = Column(Text)
    show_on_main = Column(Boolean, default=True)