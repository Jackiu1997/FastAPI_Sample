import dao
from common import get_mysql
from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate
from models import schemas
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/activity",
    tags=["activity"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.ActivityResponse])
def list(db: Session = Depends(get_mysql)):
    db_activity_list = dao.db_list_activity(db)
    return paginate(db_activity_list)


@router.post("/add", response_model=schemas.ActivityResponse)
def add(activity: schemas.ActivityRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()

    db_activity = dao.db_add_activity(db, activity, username)
    return db_activity


@router.post("/modify")
def modify(activity: schemas.ActivityRequest,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_modify_activity(db, activity)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Modify Activity {"Success" if result else "Failed"}',
    )


@router.post("/delete/{id}")
def delete(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()

    result = dao.db_delete_activity(db, id)
    raise HTTPException(
        status_code=200 if result else 400,
        detail=f'Delete Activity {"Success" if result else "Failed"}',
    )
