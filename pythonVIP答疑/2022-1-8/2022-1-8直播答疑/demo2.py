# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

from pymysql import *

# 2 创建数据库连接
conn = connect(host='localhost', port=3306, user='root', password='123456', db='test', charset='utf8')
print(conn)
# 3 打开游标
cur = conn.cursor()

cur.execute('select * from t_student') #sql语句
result = cur.fetchall() # 查询所有数据
for row in result:
    print(row)

cur.close()
conn.close()

#redis操作数据库是一个字典格式
import redis   #用于连接redis数据库的模块 ，第三方，需要安装才可能使用  pip install redis
import json
ip='127.0.0.1'
#创建对象  模块名.类名()
r=redis.Redis(host=ip,port=6379,db=0) #创建出了redis数据库对象
#字典形式
data={'name':'ysj','age':18,'gender':'女'} #类型是dict
#首先将字典转成字符串类型
new_data=json.dumps(data)

r.set('data',new_data)  #data是key，new_data是值




