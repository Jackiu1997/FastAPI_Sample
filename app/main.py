# -*- coding: utf-8 -*-
#
# 全局入口文件
# Author: Jackiu
# Email: jackiu1997@outlook.com
# Created Time: 2021-12-22
import os
from datetime import timedelta

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_pagination import add_pagination
from pydantic.main import BaseModel

from common import init_mysql
from config import CONFIG, init_config
from utils import parse_readme

# Config 设置
init_config(env='DEV')

# FastAPI 初始化
version = "0.5.0"
title, description = parse_readme()
app = FastAPI(
    debug=CONFIG.DEBUG,
    title=title,
    description=description,
    version=version,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# 数据库初始化
init_mysql(CONFIG.SQLALCHEMY_DATABASE_URI)

# 静态目录挂载
os.makedirs(CONFIG.MEDIA_UPLOAD_DIR, exist_ok=True)
os.makedirs(CONFIG.MEDIA_TEMP_DIR, exist_ok=True)
app.mount(
    "/static",
    StaticFiles(directory=CONFIG.MEDIA_UPLOAD_DIR),
    name="static",
)

# 跨域中间件设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# JWT 校验初始化设置
class Settings(BaseModel):
    authjwt_secret_key: str = CONFIG.JWT_SECRET_KEY
    access_expires: int = timedelta(minutes=CONFIG.JWT_ACCESS_TOKEN_EXPIRES)
    refresh_expires: int = timedelta(days=30)


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exception: AuthJWTException):
    return JSONResponse(
        status_code=exception.status_code,
        content={"detail": exception.message},
    )


# 加载模块路由
from routes import (activity, auth, interest, link, member, news, publication,
                    utils)

app.include_router(auth.router)
app.include_router(news.router)
app.include_router(link.router)
app.include_router(utils.router)
app.include_router(member.router)
app.include_router(interest.router)
app.include_router(activity.router)
app.include_router(publication.router)

# 添加分页支持
add_pagination(app)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=CONFIG.HOST,
        port=CONFIG.PORT,
        reload=True,
        debug=True,
    )
