from sqlalchemy.orm import Session
import models.entities as entities
import models.schemas as schemas


def db_get_user(db: Session, user: str):
    return db.query(
        entities.Users).filter(entities.Users.username == user).first()


def db_create_user(db: Session, user: schemas.UserRequest):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = entities.Users(username=user.username,
                             hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  # 刷新
    return db_user