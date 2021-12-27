from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.entities import Base

SessionLocal = None


def init_mysql(url: str):
    # echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
    engine = create_engine(url, encoding='utf8', echo=True)

    # SQLAlchemy中，CRUD是通过会话进行管理的，所以需要先创建会话，
    # 每一个SessionLocal实例就是一个数据库session
    # flush指发送到数据库语句到数据库，但数据库不一定执行写入磁盘
    # commit是指提交事务，将变更保存到数据库文件中
    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # 数据库初始化并创建
    Base.metadata.create_all(bind=engine)


def get_mysql():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    global SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()