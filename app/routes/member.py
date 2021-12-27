import dao
from common import get_mysql
from fastapi import Depends
from fastapi.routing import APIRoute
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRoute(
    prefix="/member",
    tags=["member"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.MemberResponse])
def list(db: Session = Depends[get_mysql]):
    db_member_list = dao.db_list_member(db)
    return paginate(db_member_list)


@router.post("/add", response_model=schemas.MemberResponse)
def add(member: schemas.MemberRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    db_member = dao.db_add_member(db, member)
    return db_member


@router.post("/modify", response_model=schemas.MessageResponse)
def modify(member: schemas.MemberRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()

    result = dao.db_modify_member(db, member)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Member {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}", response_model=schemas.MessageResponse)
def modify(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends[get_mysql]):
    authorize.jwt_required()
    
    result = dao.db_delete_member(db, id)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Modify Member {"Success" if result else "Failed"}',
    )