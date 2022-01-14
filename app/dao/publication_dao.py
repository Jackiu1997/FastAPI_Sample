from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_list_publication(db: Session, member_id: int = -1):
    publication_list = []
    if member_id >= 0:
        member_plist = db.query(entities.PublicationMember).filter(
            entities.PublicationMember.mid == member_id, ).first()
        if not member_plist:
            raise HTTPException(status_code=404, detail="Member Not Found")
        publication_list = member_plist.member_publications
    else:
        publication_list = db.query(entities.Publications).all()
    return publication_list


def db_add_publication(
    db: Session,
    publication: schemas.PublicationRequest,
    username: str,
):
    db_publication = entities.Publications(create_user=username,
                                           title=publication.title,
                                           author=publication.author,
                                           jounal=publication.jounal,
                                           cover=publication.cover,
                                           date=publication.date,
                                           image=publication.cover,
                                           link=publication.link)
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication


def db_delete_publication(db: Session, id: int):
    db_publication = db.query(
        entities.Publications).filter(entities.Publications.id == id).first()
    if not db_publication:
        return False
    db.delete(db_publication)
    db.commit()
    return True


def db_modify_publication(db: Session,
                          publication: schemas.PublicationResponse):
    db_publication = db.query(entities.Publications).filter(
        entities.Publications.id == publication.id).first()
    if not db_publication:
        return False
    db_publication.title = publication.title
    db_publication.author = publication.author
    db_publication.jounal = publication.jounal
    db_publication.date = publication.date
    db_publication.cover = publication.cover
    db_publication.link = publication.link
    db.commit()
    return True