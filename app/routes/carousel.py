import dao
from common import get_mysql
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from fastapi_pagination import Page, paginate
from models import schemas
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix="/carousel",
    tags=["carousel"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/list", response_model=Page[schemas.CarouselResponse])
def list(db: Session = Depends(get_mysql)):
    db_carousel_list = dao.db_list_carousel(db)
    return paginate(db_carousel_list)


@router.post("/add", response_model=schemas.CarouselResponse)
def add(carousel: schemas.CarouselRequest,
        authorize: AuthJWT = Depends(),
        db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    
    db_carousel = dao.db_add_carousel(db, carousel, username)
    return db_carousel


@router.post("/delete/{id}", response_model=schemas.MessageResponse)
def modify(id: int,
           authorize: AuthJWT = Depends(),
           db: Session = Depends(get_mysql)):
    authorize.jwt_required()
    
    result = dao.db_delete_carousel(db, id)
    return schemas.MessageResponse(
        status=200 if result else 401,
        message=f'Delete Carousel {"Success" if result else "Failed"}',
    )
