# 通过执行命令创建数据的表

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from Shopping import create_app
from comment.models import db

# 初始化app
app = create_app('develop')
manager = Manager(app)
Migrate(app, db)
manager.add_command('shopping_db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

