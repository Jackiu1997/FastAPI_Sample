from sqlalchemy import Column, Integer, String, Text
from .base import Base


class Members(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(32), unique=True, index=True, nullable=False, comment="姓名")
    avatar = Column(String(32), comment="头像")
    education = Column(Text, nullable=False, comment="学历")
    graduated = Column(Text, nullable=False, comment="毕业院校")
    research_background = Column(Text, comment="科研背景")
    email = Column(String(32), nullable=False, comment="邮箱")
    telephone = Column(String(15), comment="电话")
    address = Column(Text, comment="地址")
    tutor = Column(String(32), comment="导师")
    category = Column(Integer, default=0, comment="成员类型：0=现有成员, 1=毕业校友, 2=合作者")