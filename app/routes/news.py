import dao
from common import get_mysql
from fastapi import Depends
from fastapi.routing import APIRoute
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRoute(
    prefix="/news",
    tags=["news"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.NewsResponse])
def list(db: Session = Depends[get_mysql]):
    db_news_list = dao.db_list_news(db)
    return paginate(db_news_list)


@router.post("/add", response_model=schemas.NewsResponse)
def add(news: schemas.NewsRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    db_news = dao.db_add_news(db, news)
    return db_news


@router.post("/modify", response_model=schemas.MessageResponse)
def modify(news: schemas.NewsRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()

    result = dao.db_modify_news(db, news)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify News {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}", response_model=schemas.MessageResponse)
def modify(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    result = dao.db_delete_news(db, id)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify News {"Success" if result else "Failed"}',
    )