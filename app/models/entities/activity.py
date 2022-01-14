from sqlalchemy import Column, Integer, Text, Time
from .base import Base


class Activities(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=False, comment="标题")
    content = Column(Text, nullable=False, comment="内容")
    date = Column(Text, comment="举办日期")
    image = Column(Text, comment="图片集")