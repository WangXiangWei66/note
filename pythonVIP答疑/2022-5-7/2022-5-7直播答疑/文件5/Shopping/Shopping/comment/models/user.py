from comment.models import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash    # 生成哈希密文, 检查哈希密文

# 用户的模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), doc='用户名')
    # 数据库表中存放加密之后的密文，采用flask提供的hash算法：将生成一个128位的密文
    password = db.Column(db.String(128), doc='密码')
    icon = db.Column(db.String(5000), doc='用户头像图片')
    email = db.Column(db.String(100), doc='邮箱')
    nick_name = db.Column(db.String(200), doc='昵称')
    note = db.Column(db.String(500), doc='备注')
    phone = db.Column(db.String(11), doc='手机号')


    login_time = db.Column(db.DateTime, default=datetime.now(), doc='登录时间')
    create_time = db.Column(db.DateTime, default=datetime.now(), doc='用户注册的时间')
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), doc='用户更新的时间')
    status = db.Column(db.Integer, doc='用户状态')  # 0 代表正常

    # 是一个pwd属性的getter函数
    @property   # 代表的属性的getter函数
    def pwd(self):
        return self.password密

    # 是一个pwd属性的setter函数
    @pwd.setter    # 代表属性名setter函数
    def pwd(self, x_password):
        """
        根据明文密码，转换成密文
        :param x_password: 密码明文
        :return: 加密的密文
        """
        self.password = generate_password_hash(x_password)  # 根据flask提供的密文来加密


    def check_password(self, x_password):
        """
        验证密码
        :param x_password: 明文
        :return:
        """
        return check_password_hash(self.password, x_password)