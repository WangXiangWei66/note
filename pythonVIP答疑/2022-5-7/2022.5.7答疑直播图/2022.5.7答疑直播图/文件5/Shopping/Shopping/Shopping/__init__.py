from flask import Flask
from settings import map_config


# 负责创建App对象
def create_app(config_type):
    app = Flask(__name__)
    # 加载项目所需配置
    app.config.from_object(map_config.get(config_type))

    # 初始化限流器
    from comment.utils.limiter import limiter
    limiter.init_app(app)



    # 加载日志处理的工具
    from comment.utils.loging import create_logger
    create_logger(app)

    # 初始化sqlalchemy
    from comment.models import db
    db.init_app(app)

    # 初始化redis数据库的连接


    # 加载模块蓝图
    from Shopping.resources.user import user_bp
    app.register_blueprint(user_bp)


    return app
