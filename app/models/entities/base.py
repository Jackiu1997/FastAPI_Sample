from datetime import datetime
from typing import Any
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql.sqltypes import String


@as_declarative()
class Base:
    __name__: str

    id: Any
    create_time = Column(DateTime, default=datetime.now(), comment="创建时间")
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now(), comment="更新时间")
    is_delete = Column(Integer, default=0, comment="逻辑删除: 0=未删除, 1=删除")
    create_user = Column(String(32), comment="创建用户")

    @declared_attr
    def __tablename__(cls) -> str:
        import re
        name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        return "_".join(name_list).lower() 