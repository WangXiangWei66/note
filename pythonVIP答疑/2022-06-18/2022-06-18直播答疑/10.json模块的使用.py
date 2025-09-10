# coding:utf-8
# author:杨淑娟
import json

# 字典不是json对象，字典是dict对象 ， 只不过{"a":123,"b":456} 这种格式是json所能识别的格式
# 序列化
# （1）将字典转为字符串
dict_json={'a':123,'b':456}   # 字典类型
s=json.dumps(dict_json)    # 将字典类型，转成了字符串类型
#print(s,type(s))

#  （1）将字典转为字符串（格式化的字串)
format_s=json.dumps(dict_json,indent=4)
#print(format_s)

# # (2)将字典写进文件  ，文件中的内容是字符串
file_object=open('b.json','w')  # 创建文件对象
json.dump(dict_json,file_object)  # 将dict中的数据，写进以.json结尾的文件

# 如何读取a.json中的内容，最普通的方法,使用open ,没有读到数据
# with open('a.json','r') as file:
#     ss=file.read()
#     print(ss,type(ss)) # 字符串类型


# 反序列化
# （3）将字符串转成字典

dict_s='{"a":"123","b":"456"}'  # 字符串类型
dict_obj=json.loads(dict_s)   # 将字符串类型转成字典类型
print(dict_obj,type(dict_obj))




# （3）读取文件中的数据并转成字典

file_obj=open('a.json','r')  # 创建文件对象
data=json.load(file_obj)   # 从文件中读取数据，直接转成了dict类型
print(data,type(data))


#

