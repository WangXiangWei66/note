# 咚宝商场项目的入口

from Shopping import create_app


app = create_app("develop")

if __name__ == '__main__':
    app.run(port=5000)
