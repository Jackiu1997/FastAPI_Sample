from sqlalchemy import Column, Integer, Text, Time
from .base import Base


class Carousels(Base):
    __tablename__ = "carousels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image = Column(Text, comment="轮播图片")