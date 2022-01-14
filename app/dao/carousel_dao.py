from venv import create
from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_list_carousel(db: Session):
    carousel_list = db.query(entities.Carousels).all()
    return carousel_list


def db_add_carousel(
    db: Session,
    carousel: schemas.CarouselRequest,
    username: str,
):
    db_carousel = entities.Carousels(create_user=username,
                                     image=carousel.image)
    db.add(db_carousel)
    db.commit()
    db.refresh(db_carousel)
    return db_carousel


def db_delete_carousel(db: Session, id: int):
    db_carousel = db.query(
        entities.Carousels).filter(entities.Carousels.id == id).first()
    if not db_carousel:
        return False
    db.delete(db_carousel)
    db.commit()
    return True