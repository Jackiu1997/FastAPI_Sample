2021-12-26 19:16:53,401 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'sql_mode'2021-12-26 19:16:53,401 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-26 19:16:53,406 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2021-12-26 19:16:53,407 INFO sqlalchemy.engine.Engine [generated in 0.00058s] {}
2021-12-26 19:16:53,420 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2021-12-26 19:16:53,420 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-26 19:16:53,422 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-12-26 19:16:53,424 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,425 INFO sqlalchemy.engine.Engine [generated in 0.00052s] {'table_schema': 'shupage', 'table_name': 'activities'}
2021-12-26 19:16:53,426 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,427 INFO sqlalchemy.engine.Engine [cached since 0.002623s ago] {'table_schema': 'shupage', 'table_name': 'interests'}
2021-12-26 19:16:53,429 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,430 INFO sqlalchemy.engine.Engine [cached since 0.005768s ago] {'table_schema': 'shupage', 'table_name': 'links'}
2021-12-26 19:16:53,432 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,433 INFO sqlalchemy.engine.Engine [cached since 0.008942s ago] {'table_schema': 'shupage', 'table_name': 'members'}
2021-12-26 19:16:53,436 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,436 INFO sqlalchemy.engine.Engine [cached since 0.01225s ago] {'table_schema': 'shupage', 'table_name': 'news'}
2021-12-26 19:16:53,439 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,439 INFO sqlalchemy.engine.Engine [cached since 0.0151s ago] {'table_schema': 'shupage', 'table_name': 'publications'}
2021-12-26 19:16:53,442 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:53,442 INFO sqlalchemy.engine.Engine [cached since 0.018s ago] {'table_schema': 'shupage', 'table_name': 'users'}
2021-12-26 19:16:53,447 INFO sqlalchemy.engine.Engine 
CREATE TABLE activities (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        title TEXT NOT NULL COMMENT '????????????',
        content TEXT NOT NULL COMMENT '????????????',
        hold_date TEXT COMMENT '????????????',
        image TEXT COMMENT '????????????',
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,449 INFO sqlalchemy.engine.Engine [no key 0.00203s] {}
2021-12-26 19:16:53,475 INFO sqlalchemy.engine.Engine CREATE INDEX ix_activities_id ON activities (id)
2021-12-26 19:16:53,476 INFO sqlalchemy.engine.Engine [no key 0.00099s] {}
2021-12-26 19:16:53,495 INFO sqlalchemy.engine.Engine 
CREATE TABLE interests (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        title TEXT NOT NULL COMMENT '????????????',
        content TEXT NOT NULL COMMENT '????????????',
        image TEXT COMMENT '????????????',
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,497 INFO sqlalchemy.engine.Engine [no key 0.00216s] {}
2021-12-26 19:16:53,518 INFO sqlalchemy.engine.Engine CREATE INDEX ix_interests_id ON interests (id)
2021-12-26 19:16:53,518 INFO sqlalchemy.engine.Engine [no key 0.00073s] {}
2021-12-26 19:16:53,537 INFO sqlalchemy.engine.Engine 
CREATE TABLE links (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        title TEXT NOT NULL COMMENT '????????????',
        content TEXT COMMENT '????????????',
        image TEXT COMMENT '????????????',
        url TEXT COMMENT '??????URL',
        category INTEGER COMMENT '???????????????0=Jounal Links, 1=Jounal Clubs, 2=Useful Links, 3=Group Links',
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,539 INFO sqlalchemy.engine.Engine [no key 0.00215s] {}
2021-12-26 19:16:53,557 INFO sqlalchemy.engine.Engine CREATE INDEX ix_links_id ON links (id)
2021-12-26 19:16:53,557 INFO sqlalchemy.engine.Engine [no key 0.00066s] {}
2021-12-26 19:16:53,577 INFO sqlalchemy.engine.Engine 
CREATE TABLE members (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        name VARCHAR(32) NOT NULL COMMENT '????????????',
        avatar VARCHAR(32) COMMENT '????????????',
        education TEXT NOT NULL COMMENT '??????',
        graduated TEXT NOT NULL COMMENT '????????????',
        education_detail TEXT COMMENT '????????????',
        email VARCHAR(32) NOT NULL COMMENT '????????????',
        telephone VARCHAR(15) COMMENT '????????????',
        address TEXT COMMENT '????????????',
        tutor VARCHAR(32) COMMENT '????????????',
        category INTEGER COMMENT '???????????????0=????????????, 1=????????????, 2=?????????',
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,580 INFO sqlalchemy.engine.Engine [no key 0.00270s] {}
2021-12-26 19:16:53,599 INFO sqlalchemy.engine.Engine CREATE INDEX ix_members_id ON members (id)
2021-12-26 19:16:53,599 INFO sqlalchemy.engine.Engine [no key 0.00046s] {}
2021-12-26 19:16:53,618 INFO sqlalchemy.engine.Engine CREATE UNIQUE INDEX ix_members_name ON members (name)
2021-12-26 19:16:53,618 INFO sqlalchemy.engine.Engine [no key 0.00044s] {}
2021-12-26 19:16:53,636 INFO sqlalchemy.engine.Engine 
CREATE TABLE news (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        title TEXT NOT NULL COMMENT '????????????',
        abstract TEXT COMMENT '????????????',
        content TEXT COMMENT '????????????',
        show_on_main BOOL COMMENT '??????????????????',
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,638 INFO sqlalchemy.engine.Engine [no key 0.00200s] {}
2021-12-26 19:16:53,655 INFO sqlalchemy.engine.Engine CREATE INDEX ix_news_id ON news (id)
2021-12-26 19:16:53,655 INFO sqlalchemy.engine.Engine [no key 0.00040s] {}
2021-12-26 19:16:53,673 INFO sqlalchemy.engine.Engine 
CREATE TABLE publications (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        jounal TEXT,
        cover TEXT,
        publish_date VARCHAR(32),
        link TEXT,
        show_on_main BOOL,
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,676 INFO sqlalchemy.engine.Engine [no key 0.00278s] {}
2021-12-26 19:16:53,695 INFO sqlalchemy.engine.Engine CREATE INDEX ix_publications_id ON publications (id)
2021-12-26 19:16:53,696 INFO sqlalchemy.engine.Engine [no key 0.00048s] {}
2021-12-26 19:16:53,714 INFO sqlalchemy.engine.Engine 
CREATE TABLE users (
        create_time DATETIME COMMENT '????????????',
        update_time DATETIME COMMENT '????????????',
        is_delete INTEGER COMMENT '????????????: 0=?????????, 1=??????',
        create_user VARCHAR(32) COMMENT '????????????',
        id INTEGER NOT NULL AUTO_INCREMENT,
        username VARCHAR(32) NOT NULL,
        hashed_password VARCHAR(32) NOT NULL,
        is_active BOOL,
        PRIMARY KEY (id)
)


2021-12-26 19:16:53,716 INFO sqlalchemy.engine.Engine [no key 0.00211s] {}
2021-12-26 19:16:53,733 INFO sqlalchemy.engine.Engine CREATE UNIQUE INDEX ix_users_username ON users (username)
2021-12-26 19:16:53,734 INFO sqlalchemy.engine.Engine [no key 0.00048s] {}
2021-12-26 19:16:53,751 INFO sqlalchemy.engine.Engine CREATE INDEX ix_users_id ON users (id)
2021-12-26 19:16:53,752 INFO sqlalchemy.engine.Engine [no key 0.00048s] {}
2021-12-26 19:16:53,765 INFO sqlalchemy.engine.Engine COMMIT
INFO:     Will watch for changes in these directories: ['D:\\Workspace\\Python\\????????????\\backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15752] using watchgod
2021-12-26 19:16:56,314 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'sql_mode'
2021-12-26 19:16:56,316 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-26 19:16:56,322 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2021-12-26 19:16:56,322 INFO sqlalchemy.engine.Engine [generated in 0.00066s] {}
2021-12-26 19:16:56,327 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2021-12-26 19:16:56,328 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-26 19:16:56,331 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-12-26 19:16:56,334 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,334 INFO sqlalchemy.engine.Engine [generated in 0.00096s] {'table_schema': 'shupage', 'table_name': 'activities'}
2021-12-26 19:16:56,337 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,337 INFO sqlalchemy.engine.Engine [cached since 0.004248s ago] {'table_schema': 'shupage', 'table_name': 'interests'}
2021-12-26 19:16:56,339 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,341 INFO sqlalchemy.engine.Engine [cached since 0.006984s ago] {'table_schema': 'shupage', 'table_name': 'links'}
2021-12-26 19:16:56,342 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,343 INFO sqlalchemy.engine.Engine [cached since 0.01002s ago] {'table_schema': 'shupage', 'table_name': 'members'}
2021-12-26 19:16:56,347 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,348 INFO sqlalchemy.engine.Engine [cached since 0.01493s ago] {'table_schema': 'shupage', 'table_name': 'news'}
2021-12-26 19:16:56,350 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,351 INFO sqlalchemy.engine.Engine [cached since 0.01775s ago] {'table_schema': 'shupage', 'table_name': 'publications'}
2021-12-26 19:16:56,353 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,355 INFO sqlalchemy.engine.Engine [cached since 0.02104s ago] {'table_schema': 'shupage', 'table_name': 'users'}
2021-12-26 19:16:56,358 INFO sqlalchemy.engine.Engine COMMIT
WARNING:  The --reload flag should not be used in production on Windows.
2021-12-26 19:16:56,756 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'sql_mode'
2021-12-26 19:16:56,759 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-26 19:16:56,762 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2021-12-26 19:16:56,763 INFO sqlalchemy.engine.Engine [generated in 0.00073s] {}
2021-12-26 19:16:56,767 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2021-12-26 19:16:56,768 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-12-26 19:16:56,770 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-12-26 19:16:56,772 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,773 INFO sqlalchemy.engine.Engine [generated in 0.00133s] {'table_schema': 'shupage', 'table_name': 'activities'}
2021-12-26 19:16:56,776 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,776 INFO sqlalchemy.engine.Engine [cached since 0.00477s ago] {'table_schema': 'shupage', 'table_name': 'interests'}
2021-12-26 19:16:56,779 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,780 INFO sqlalchemy.engine.Engine [cached since 0.008043s ago] {'table_schema': 'shupage', 'table_name': 'links'}
2021-12-26 19:16:56,782 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,783 INFO sqlalchemy.engine.Engine [cached since 0.01157s ago] {'table_schema': 'shupage', 'table_name': 'members'}
2021-12-26 19:16:56,786 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,787 INFO sqlalchemy.engine.Engine [cached since 0.01563s ago] {'table_schema': 'shupage', 'table_name': 'news'}
2021-12-26 19:16:56,791 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,792 INFO sqlalchemy.engine.Engine [cached since 0.02009s ago] {'table_schema': 'shupage', 'table_name': 'publications'}
2021-12-26 19:16:56,794 INFO sqlalchemy.engine.Engine SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %(table_schema)s AND table_name = %(table_name)s
2021-12-26 19:16:56,795 INFO sqlalchemy.engine.Engine [cached since 0.02316s ago] {'table_schema': 'shupage', 'table_name': 'users'}
2021-12-26 19:16:56,797 INFO sqlalchemy.engine.Engine COMMIT
INFO:     Started server process [10304]
INFO:     Waiting for application startup.
INFO:     Application startup complete