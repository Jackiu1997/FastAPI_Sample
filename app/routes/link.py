import dao
from common import get_mysql
from fastapi import Depends
from fastapi.routing import APIRoute
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRoute(
    prefix="/link",
    tags=["link"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.LinkResponse])
def list(db: Session = Depends[get_mysql]):
    db_link_list = dao.db_list_link(db)
    return paginate(db_link_list)


@router.post("/add", response_model=schemas.LinkResponse)
def add(link: schemas.LinkRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    db_link = dao.db_add_link(db, link)
    return db_link


@router.post("/modify", response_model=schemas.MessageResponse)
def modify(link: schemas.LinkRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()

    result = dao.db_modify_link(db, link)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Link {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}", response_model=schemas.MessageResponse)
def modify(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    result = dao.db_delete_link(db, id)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Link {"Success" if result else "Failed"}',
    )