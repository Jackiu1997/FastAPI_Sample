from sqlalchemy import Column, Integer, Text
from .base import Base


class Links(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(Text, nullable=False, comment="标题")
    content = Column(Text, comment="描述")
    image = Column(Text, comment="图片")
    url = Column(Text, comment="链接URL")
    category = Column(
        Integer,
        default=0,
        comment="链接类型：0=Jounal Links, 1=Jounal Clubs, 2=Useful Links, 3=Group Links",
    )
