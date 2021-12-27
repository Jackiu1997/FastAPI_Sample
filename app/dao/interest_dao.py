from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_list_interest(db: Session):
    interest_list = db.query(entities.Interests).all()
    return interest_list


def db_add_interest(db: Session, interest: schemas.InterestRequest):
    db_interest = entities.Interests(title=interest.title,
                                     content=interest.content,
                                     image=interest.image)
    db.add(db_interest)
    db.commit()
    db.refresh(db_interest)
    return db_interest


def db_delete_interest(db: Session, id: int):
    db_interest = db.query(
        entities.Interests).filter(entities.Interests.id == id).first()
    if not db_interest:
        return False
    db.delete(db_interest)
    db.commit()
    return True

def db_modify_activity(db: Session, interest: schemas.InterestResponse):
    db_interest = db.query(
        entities.Activities).filter(entities.Activities.id == interest.id).first()
    if not db_interest:
        return False
    db_interest.title = interest.title
    db_interest.content = interest.content
    db_interest.image = interest.image
    db.commit()
    return True