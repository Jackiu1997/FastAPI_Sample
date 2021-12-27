class Config(object):
    # 是否调试模式
    DEBUG = False

    # 默认端口 8000
    PORT = 8000

    # 默认主机 localhost
    HOST = '127.0.0.1'

    # 数据库连接设置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = ""

    # JWT Token 设置
    JWT_SECRET_KEY = '计算机学院党建token数字签名'
    JWT_BLACKLIST_ENABLED = False
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24 * 7

    # 图像上传设置
    IMAGE_LIMIT_SIZE = 5 * 1024 * 1024  # 5M
    MEDIA_UPLOAD_DIR = "media/static"
    MEDIA_TEMP_DIR = "media/temp"


class DevelopmentConfig(Config):
    """ 开发环境配置 """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/shupage?charset=utf8"


class ProductionConfig(Config):
    """ 生产环境配置 """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/shupage?charset=utf8"


class TestConfig(Config):
    """ 测试环境配置 """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/shupage?charset=utf8"