import dao
from common import get_mysql
from fastapi import Depends
from fastapi.routing import APIRoute
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRoute(
    prefix="/interest",
    tags=["interest"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.InterestResponse])
def list(db: Session = Depends[get_mysql]):
    db_interest_list = dao.db_list_interest(db)
    return paginate(db_interest_list)


@router.post("/add", response_model=schemas.InterestResponse)
def add(interest: schemas.InterestRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    db_interest = dao.db_add_interest(db, interest)
    return db_interest


@router.post("/modify", response_model=schemas.MessageResponse)
def modify(interest: schemas.InterestRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()

    result = dao.db_modify_interest(db, interest)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Interest {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}", response_model=schemas.MessageResponse)
def modify(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    result = dao.db_delete_interest(db, id)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Interest {"Success" if result else "Failed"}',
    )