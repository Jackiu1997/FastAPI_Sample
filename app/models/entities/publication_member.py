from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from .base import Base


class PublicationMember(Base):
    __tablename__ = "publication_member"
    mid = Column(Integer, ForeignKey("members.id"), primary_key=True)
    pid = Column(Integer, ForeignKey("publications.id"), primary_key=True)

    publication = relationship("Publications", backref="member_publications")