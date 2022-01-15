import dao
from common import get_mysql
from fastapi import Depends, APIRouter, HTTPException
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/news",
    tags=["news"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.NewsResponse])
def list(db: Session = Depends(get_mysql)):
    db_news_list = dao.db_list_news(db)
    return paginate(db_news_list)


@router.post("/add", response_model=schemas.NewsResponse)
def add(news: schemas.NewsRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    
    db_news = dao.db_add_news(db, news, username)
    return db_news


@router.post("/modify")
def modify(news: schemas.NewsRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_modify_news(db, news)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Modify News {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}")
def delete(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    
    result = dao.db_delete_news(db, id)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Delete News {"Success" if result else "Failed"}',
    )