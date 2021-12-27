from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_list_member(db: Session):
    member_list = db.query(entities.Members).all()
    return member_list


def db_add_member(db: Session, member: schemas.MemberRequest):
    db_member = entities.Members(name=member.name,
                                 avatar=member.avatar,
                                 education=member.education,
                                 graduated=member.graduated,
                                 research_background=member.research_background,
                                 email=member.email,
                                 telephone=member.telephone,
                                 address=member.address,
                                 tutor=member.tutor,
                                 category=member.category)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def db_delete_member(db: Session, id: int):
    db_member = db.query(
        entities.Members).filter(entities.Members.id == id).first()
    if not db_member:
        return False
    db.delete(db_member)
    db.commit()
    return True


def db_modify_member(db: Session, member: schemas.MemberResponse):
    db_member = db.query(
        entities.Members).filter(entities.Members.id == member.id).first()
    if not db_member:
        return False
    db_member.name = member.name
    db_member.avatar = member.avatar
    db_member.education = member.education
    db_member.graduated = member.graduated
    db_member.research_background = member.research_background
    db_member.email = member.email
    db_member.telephone = member.telephone
    db_member.address = member.address
    db_member.tutor = member.tutor
    db_member.category = member.category  # TODO: type 校验
    db.commit()
    return True