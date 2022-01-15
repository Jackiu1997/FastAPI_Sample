from typing import Optional
import dao
from common import get_mysql
from fastapi import Depends, APIRouter, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate
from models import schemas
from sqlalchemy.orm.session import Session

from models.entities import user

router = APIRouter(
    prefix="/publication",
    tags=["publication"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.PublicationResponse])
def list(member_id: Optional[int] = -1, db: Session = Depends(get_mysql)):
    db_publication_list = dao.db_list_publication(db, member_id=member_id)
    return paginate(db_publication_list)


@router.post("/add", response_model=schemas.PublicationResponse)
def add(publication: schemas.PublicationRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()

    db_publication = dao.db_add_publication(db, publication, username)
    return db_publication


@router.post("/modify")
def modify(publication: schemas.PublicationRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_modify_publication(db, publication)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Modify Publication {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}")
def delete(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_delete_publication(db, id)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Delete Publication {"Success" if result else "Failed"}',
    )