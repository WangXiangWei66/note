# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 将Excel数据存储到Mysql中
# 操作数据库需要按装一个模块pymysql
import  pandas as pd
# sqlalchemy需要安装   ，pip install  sqlalchemy

# 还需要去安装一个叫pymysql模块  pip install pymysql
from sqlalchemy import create_engine # 用于去创建数据库引擎
df=pd.read_excel('世界各国粮食产量排名.xlsx')

# 保存到数据库中 用户名:root，密码123456 ,主机 本机可以使用localhost,127.0.0.1, Mysql的端口号是3306，数据库的名称test
#  可以变的，用户名，密码，数据库名
yconnect=create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
#print(yconnect)
df.to_sql('student2',con=yconnect,index=False) # 保存到数据库中，不保存索引，要求student表在数据库中不存在


