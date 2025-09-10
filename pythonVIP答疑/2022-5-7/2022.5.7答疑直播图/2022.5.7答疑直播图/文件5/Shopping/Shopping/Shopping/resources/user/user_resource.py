from flask_restful import Resource
from flask import current_app, request
from comment.utils.shopping_redis import redis_client
import json
from comment.utils.limiter import limiter as lmt
from Shopping.resources.user import constants
from flask_limiter.util import get_remote_address
import random
from comment.utils.aliyun_sms_send import send_sms
from flask_restful.reqparse import RequestParser
from comment.utils import parser
from comment.models.user import User
from comment.models import db

# 用于测试的资源类
class Shopping_User(Resource):
    def get(self):
        current_app.logger.info("我的测试日志")
        # 这里的代码可能会用到User模型类
        return {'hello': '测试'}


# 用于测试短信发送
class User_SMS(Resource):
    """发送验证码的短信"""
    error_message = 'too many requests'
    decorators = [
        # 三个参数：参数1：限制速率 参数2：key_func 参数3：如果超出限制之后的提示信息
        lmt.limit(constants.LIMIT_SMS_CODE_BY_MOBILE,   # 根据手机号的限制器
                  key_func=lambda: request.args['phone'],
                  error_message=error_message),
        lmt.limit(constants.LIMIT_SMS_CODE_BY_IP,       # 根据服务端IP进行限制
                  key_func=get_remote_address,       # 用于得到客户端的远程地址
                  error_message=error_message)
    ]

    def get(self):
        phone = request.args['phone'].strip()
        code = random.randint(1000, 9999)
        result = send_sms(phone, str(code))  # 返回的是json的字符串
        result = json.loads(result)  # 把json编程字典
        # result 往里面添加手机号码
        result['phone'] = phone

        # 短信验证码发送成功之后，还需要把验证码存放到redis数据库中，以便于下次验证，验证码的时效为5分钟
        redis_client.setex('shopping:code:{}'.format(phone), constants.SMS_CODE_EXPIRES, code)  # 参数1：key,参数2：时效

        return result


# 验证手机号与验证码是否匹配
class AuthorizationCodeResource(Resource):
    """
    提交手机号和验证码开始验证
    """
    def post(self):
        rp = RequestParser()
        rp.add_argument('phone', type=parser.mobile, required=True)
        rp.add_argument('code', type=parser.regex(r'^/d{4}$'), required=True)
        args = rp.parse_args()
        phone = args.phone
        code = args.code

        # 从redis数据库中得到之前保存的验证码
        key = 'shopping:code:{}'.format(phone)
        try:
            real_code = redis_client.get(key)   # 从redis中返回的是字节数据
        except ConnectionError as e:
            current_app.logger.error(e)
            return {'message': 'redis db connect error'}, 400

        # 开始校验
        if not real_code or real_code.decode() != code:
            return {'message': 'Invalid code'}, 400     # 校验失败

        # 校验成功
        return {'phone': phone, 'msg': 'code success'}


class RegisterUserResource(Resource):

    '''
    填写账户信息，完成用户注册
    '''
    def post(self):
        rp = RequestParser()
        rp.add_argument('phone', type=parser.mobile, required=True)
        rp.add_argument('username', required=True)
        rp.add_argument('password', required=True)
        rp.add_argument('email', type=parser.email, required=True)
        args = rp.parse_args()
        username = args.username
        password = args.password
        phone = args.phone
        email = args.email


        # 验证用户名是否唯一： 先从Mysql数据库中根据当前用户名查询
        u = User.query.filter(User.username == username).first()
        if u:   # 用户已经存在
            current_app.logger.info('{}:用户已存在'.format(username))
            return {'msg': "The username already exists."}, 400

        # 用户信息保存到数据库中
        u = User(username=username, pwd=password, email=email, status=0)   # pwd代表 运用函数加密之后的密文
        db.session.add(u)   # 将验证好的数据添加到数据库中
        db.session.commit()
        return {'msg': 'OK'}







