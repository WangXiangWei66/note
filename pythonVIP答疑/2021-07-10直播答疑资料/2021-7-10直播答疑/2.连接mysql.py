#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
#如何用代码查看存储在mysql中的数据
# 安装第三方模块pymysql   --》pip install pymysql
# (1)导入
from pymysql import *

#(2)创建连接  host= IP地址  mysql，
conn=connect(host='localhost',port=3306,user='root',password='123456',db='test' ,charset='utf8')
#print(conn)\

# (3)打开游标
cur=conn.cursor()

# (4)编写sql语句 (数据库里需要有student这个表)
sql='select * from student where 语文>=%s and 数学>%s' # *%占位符，占的是查询条件的值的位置

params=(80,97) # 给%s赋值

#（5）执行sql语句
cur.execute(sql,params)

#（6）读取查询结果(符合条件的全部查询结果)
result=cur.fetchall()
for item in result:
    print(item)

# （7）关闭
cur.close()
#（８）关闭连接
conn.close()