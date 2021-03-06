from typing import List
import dao
from common import get_mysql
from fastapi import Depends, APIRouter, HTTPException
from fastapi_jwt_auth import AuthJWT
from models import schemas
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/link",
    tags=["link"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=List[schemas.LinkResponse])
def list(db: Session = Depends(get_mysql)):
    db_link_list = dao.db_list_link(db)
    return db_link_list


@router.post("/add", response_model=schemas.LinkResponse)
def add(link: schemas.LinkRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    
    db_link = dao.db_add_link(db, link, username)
    return db_link


@router.post("/modify")
def modify(link: schemas.LinkRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_modify_link(db, link)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Modify Link {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}")
def delete(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    
    result = dao.db_delete_link(db, id)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Delete Link {"Success" if result else "Failed"}',
    )