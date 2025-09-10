# 当前的命令调用Flask要和Web主程序分离,  只限管理员用户测试

from flask_script import Manager
from Shopping import create_app
from flask_sqlalchemy import SQLAlchemy

app = create_app('develop')
db = SQLAlchemy(app)
manager = Manager(app)


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)


# db.create_all()   # 创建表

@manager.command
def hello():
    print('你的命令执行成功')


# 通过命令直接在数据库中创建一个用户
@manager.option("-u", "--username", dest="x_uname")
@manager.option("-p", "--password", dest="x_pwd")
def create_user(x_uname, x_pwd):
    user = User(username=x_uname, password=x_pwd)   # 这里关键字必须与创建表格关键字一致
    db.session.add(user)
    db.session.commit()
    print('执行命令添加用户成功！')


if __name__ == '__main__':
    manager.run()
