# 负责整个项目的配置信息

class Config:
    # 配置数据库和SQLAlchemy
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'test1'  # 访问数据库
    USERNAME = 'root'
    PASSWORD = 'root'

    # 编码格式根据数据库进行调整
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI    # 关于sql的url
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 用于数据库追踪的修改(会占用资源)，会以警告的方式提示，一般不需要

    # 日志的配置
    LOGGING_LEVEL = 'DEBUG'
    LOGGING_FILE_DIR = 'logs/'
    LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
    LOGGING_FILE_BACKUP = 10

    # 限流器采用Redis保存数据，默认是内存，需安装flask-redis
    RATELIMIT_STORAGE_URL = 'redis://192.168.68.132:6379/0'  # 末尾的0号数据库 代表是限流器使用的
    # 限制策略：移动窗口：时间窗口会自动化
    RATELIMIT_STRATEGY = 'moving-window'

    # redis数据库的连接地址, 使用数据1来存放缓存数据包括短信验证码
    REDIS_URL = 'redis://192.168.68.132:6379/1'


# 开发环境下的配置信息
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True   # 打印sql到日志中


# 生产环境中的配置信息
class ProductConfig(Config):
    pass

