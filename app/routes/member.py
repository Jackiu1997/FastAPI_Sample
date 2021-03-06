import dao
from common import get_mysql
from fastapi import Depends, APIRouter, HTTPException
from fastapi_jwt_auth import AuthJWT
from models import schemas
from fastapi_pagination import Page, paginate
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/member",
    tags=["member"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.MemberResponse])
def list(category = -1, db: Session = Depends(get_mysql)):
    db_member_list = dao.db_list_member(db, category=category)
    return paginate(db_member_list)


@router.post("/add", response_model=schemas.MemberResponse)
def add(member: schemas.MemberRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    
    db_member = dao.db_add_member(db, member, username)
    return db_member


@router.post("/modify")
def modify(member: schemas.MemberRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_modify_member(db, member)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Modify Member {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}")
def delete(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    
    result = dao.db_delete_member(db, id)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Delete Member {"Success" if result else "Failed"}',
    )