# coding:utf-8
# author:杨淑娟
import pymysql

import pandas as pd
#安装一个模块 sqlalchemy   -->pip install sqlalchemy
from sqlalchemy import  create_engine
                                       #用户名:密码@服务器:MySQL的端口号/数据库?数据库的编码格式
engine=create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')
data=[
    [33,'张三'],
    [44,'李四']
]
                                  #idd,name是数据库中的列表
df=pd.DataFrame(data=data,columns=['id','name'],index=[1,2])

#将DataFrame数据写到mysql数据库
         #name='stu'-->stu是表名
df.to_sql(name='stu',con=engine,if_exists='append',index=False)

