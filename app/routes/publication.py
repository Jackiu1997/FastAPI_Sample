import dao
from common import get_mysql
from fastapi import Depends
from fastapi.routing import APIRoute
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRoute(
    prefix="/publication",
    tags=["publication"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.PublicationResponse])
def list(db: Session = Depends[get_mysql]):
    db_publication_list = dao.db_list_publication(db)
    return paginate(db_publication_list)


@router.post("/add", response_model=schemas.PublicationResponse)
def add(publication: schemas.PublicationRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    db_publication = dao.db_add_publication(db, publication)
    return db_publication


@router.post("/modify", response_model=schemas.MessageResponse)
def modify(publication: schemas.PublicationRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()

    result = dao.db_modify_publication(db, publication)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Publication {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}", response_model=schemas.MessageResponse)
def modify(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    result = dao.db_delete_publication(db, id)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Publication {"Success" if result else "Failed"}',
    )