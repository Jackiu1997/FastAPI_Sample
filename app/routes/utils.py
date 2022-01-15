import hashlib
from pathlib import Path

from config import CONFIG
from fastapi import APIRouter, Depends, HTTPException
from fastapi.datastructures import UploadFile
from fastapi.params import File
from fastapi_jwt_auth import AuthJWT

router = APIRouter(
    prefix="/utils",
    tags=["utils"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/upload")
async def upload(file: UploadFile = File(...), authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    try:
        data = await file.read()
        if len(data) > CONFIG.IMAGE_LIMIT_SIZE:
            raise HTTPException(status_code=403, detail="Image Size is Limited to 5MB")

        suffix = Path(file.filename).suffix
        file_name = hashlib.md5(file).hexdigest() + suffix
        open(f"{CONFIG.MEDIA_UPLOAD_DIR}/{file_name}", 'wb').write(data)
    except:
        raise HTTPException(status_code=500, detail="Upload Image Failed")

    return {"image": f"/static/{file_name}"}
