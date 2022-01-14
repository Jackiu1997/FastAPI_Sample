from sqlalchemy import Column, Integer, String, Text, Boolean
from .base import Base


class Publications(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=False, comment="标题")
    author = Column(Text, comment="作者")
    jounal = Column(Text, comment="期刊")
    cover = Column(Text, comment="封面")
    date = Column(String(32), comment="出版日期")
    link = Column(Text, comment="链接")
    show_on_main = Column(Boolean, default=True, comment="是否主页展示")