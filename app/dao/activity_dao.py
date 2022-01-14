from venv import create
from sqlalchemy.orm import Session
import models.entities as entities
from models.entities import user
import models.schemas as schemas


def db_list_activity(db: Session):
    activity_list = db.query(entities.Activities).all()
    return activity_list


def db_add_activity(
    db: Session,
    activity: schemas.ActivityRequest,
    username: str,
):
    db_activity = entities.Activities(create_user=username,
                                      title=activity.title,
                                      content=activity.content,
                                      date=activity.date,
                                      image=activity.image)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def db_delete_activity(db: Session, id: int):
    db_activity = db.query(
        entities.Activities).filter(entities.Activities.id == id).first()
    if not db_activity:
        return False
    db.delete(db_activity)
    db.commit()
    return True


def db_modify_activity(db: Session, activity: schemas.ActivityResponse):
    db_activity = db.query(entities.Activities).filter(
        entities.Activities.id == activity.id).first()
    if not db_activity:
        return False
    db_activity.title = activity.title
    db_activity.content = activity.content
    db_activity.date = activity.date
    db_activity.image = activity.image
    db.commit()
    return True