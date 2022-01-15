from typing import List
import dao
from common import get_mysql
from fastapi import Depends, APIRouter, HTTPException
from fastapi_jwt_auth import AuthJWT
from models import schemas
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/interest",
    tags=["interest"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=List[schemas.InterestResponse])
def list(db: Session = Depends(get_mysql)):
    db_interest_list = dao.db_list_interest(db)
    return db_interest_list


@router.post("/add", response_model=schemas.InterestResponse)
def add(interest: schemas.InterestRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()

    db_interest = dao.db_add_interest(db, interest, username)
    return db_interest


@router.post("/modify")
def modify(interest: schemas.InterestRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_modify_interest(db, interest)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Modify Interest {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}")
def delete(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_delete_interest(db, id)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Delete Interest {"Success" if result else "Failed"}',
    )