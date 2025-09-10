# coding:utf-8
# author:杨淑娟
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
)

cursor = db.cursor()

def query(sql):
    cursor.execute(sql)
    row = cursor.fetchone()
    return row

print('=' * 80)
a = '马士兵教育'
s = "SELECT HEX('%s');" % a
ret = query(s)
ret = ret[0]
# E9A9ACE5A3ABE585B5E69599E882B2
print(ret)  # 把一个字符串转成十六进制字符串
step=2
from urllib.request import quote, unquote

def fun(s):
    lst=[]
    for item in range(0,len(s),2):
        lst.append('%'+s[item:item+2])
    return lst

lst=fun(ret)
y=''.join(lst)
print(y)
ret=unquote(''.join(lst),encoding='utf-8')
print(ret)

xx=''.join(y.split('%'))
print(xx)


s = "SELECT UNHEX('%s');" % xx
ret = query(s)
ret = ret[0]
print(ret, len(ret))
ret = ret.decode('utf-8')
print(ret, len(ret))
