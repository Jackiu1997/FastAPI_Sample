from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_list_link(db: Session):
    link_list = db.query(entities.Links).all()
    return link_list


def db_add_link(db: Session, link: schemas.LinkRequest):
    db_link = entities.Links(title=link.title,
                             content=link.content,
                             image=link.image,
                             url=link.url,
                             category=link.category)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


def db_delete_link(db: Session, id: int):
    db_link = db.query(entities.Links).filter(entities.Links.id == id).first()
    if not db_link:
        return False
    db.delete(db_link)
    db.commit()
    return True


def db_modify_link(db: Session, link: schemas.LinkResponse):
    db_link = db.query(entities.Links).filter(entities.Links.id == link.id).first()
    if not db_link:
        return False
    db_link.title = link.title
    db_link.content = link.content
    db_link.image = link.image
    db_link.url = link.url
    db_link.category = link.category  # TODO: type 校验
    db.commit()
    return True