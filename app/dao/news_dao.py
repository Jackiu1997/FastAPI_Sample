from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_list_news(db: Session):
    news_list = db.query(entities.News).all()
    return news_list


def db_add_news(
    db: Session,
    news: schemas.NewsRequest,
    username: str,
):
    db_news = entities.News(create_user=username,
                            title=news.title,
                            abstract=news.abstract,
                            content=news.content,
                            show_on_main=news.show_on_main)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


def db_delete_news(db: Session, id: int):
    db_news = db.query(entities.News).filter(entities.News.id == id).first()
    if not db_news:
        return False
    db.delete(db_news)
    db.commit()
    return True


def db_modify_news(db: Session, news: schemas.NewsResponse):
    db_news = db.query(
        entities.News).filter(entities.News.id == news.id).first()
    if not db_news:
        return False
    db_news.title = news.title
    db_news.abstract = news.abstract
    db_news.content = news.content
    db_news.show_on_main = news.show_on_main
    db.commit()
    return True