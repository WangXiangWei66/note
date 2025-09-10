# 用户模式下的蓝图，包括用户模块的所有资源

from flask import Blueprint
from flask_restful import Api
from comment.utils.output import output_json

user_bp = Blueprint('user', __name__, url_prefix='/user')   # 创建蓝图 用于蓝图模块找到它对应所在目录的位置
user_api = Api(user_bp)     # 创建蓝图中的资源API

# 在当前用户模块添加请求钩子
# user_bp.before_request()

# 使用我们自定义json格式，替代装饰器的写法   以便以后其他代码的使用，而不需要一个个去赋予装饰器。
user_api.representation('application/json')(output_json)


# 加载当前模块的资源
from Shopping.resources.user.user_resource import Shopping_User, User_SMS, AuthorizationCodeResource, RegisterUserResource


user_api.add_resource(Shopping_User, '/hello', endpoint='user')  # 日志蓝图
user_api.add_resource(User_SMS, '/sms', endpoint='sms')     # 短信发送蓝图
user_api.add_resource(AuthorizationCodeResource, '/authorization', endpoint='authorization')  # 验证码验证蓝图
user_api.add_resource(RegisterUserResource, '/register', endpoint='register')  # 用户注册
