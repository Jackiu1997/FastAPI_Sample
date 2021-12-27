from sqlalchemy import Column, Boolean, Integer, Text, Time
from .base import Base


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=False, comment="新闻标题")
    abstract = Column(Text, comment="新闻摘要")
    content = Column(Text, comment="新闻内容")
    show_on_main = Column(Boolean, default=False, comment="是否主页展示")