from sqlalchemy import Column, Integer, Text
from .base import Base


class Interests(Base):
    __tablename__ = "interests"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=False, comment="标题")
    content = Column(Text, nullable=False, comment="内容")
    image = Column(Text, comment="图片")