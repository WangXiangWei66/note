# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟


import  mysql.connector  # 上课时讲的
#创建连接对象
conn=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='test',auth_plugin='mysql_native_password')
print(conn)


# Python与MySQL的交互  【Python全栈中的课程】
import pymysql  # 连接MySQL数据库的模块
conn =pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='test',charset='utf8')
print(conn)


