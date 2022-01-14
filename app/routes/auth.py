import dao
from common import get_mysql
from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from models import schemas
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/regist", response_model=schemas.UserResponse)
def regist(user: schemas.UserRequest, db: Session = Depends(get_mysql)):
    db_user = dao.db_create_user(db, user)
    return db_user


@router.post("/login")
def login(user: schemas.UserRequest,
          authorize: AuthJWT = Depends(),
          db: Session = Depends(get_mysql)):
    db_user = dao.db_get_user(db, user.username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User Not Found")
    elif db_user.hashed_password != user.password + "notreallyhashed":
        raise HTTPException(status_code=401, detail="Password Wrong")

    access_token = authorize.create_access_token(subject=user.username)
    refresh_token = authorize.create_refresh_token(subject=user.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post('/refresh')
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()

    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@router.get('/protected')
def protected(authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    current_user = authorize.get_jwt_subject()
    return {"user": current_user}
