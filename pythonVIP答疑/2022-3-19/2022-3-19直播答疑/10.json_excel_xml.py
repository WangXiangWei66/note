# coding:utf-8
# author:杨淑娟
import json     # 导入模块，  操作json文件
import  openpyxl  # 导入模块，  操作Excel文件
from xml.dom.minidom import  Document # 导入模块 ，  操作XML文件

# 定义一个字符串
s='{"name":"张三","age":20}'

# 将数据以json格式写到a.txt文件中 ，ensure_ascii=False 正确显示中文
json.dump(s,open('a.txt','w',encoding='utf-8'),ensure_ascii=False)

# 从文件中读取数据
sload=json.load(open('a.txt','r',encoding='utf-8'))
print(type(sload)) # str字符串类型

d=eval(sload)   # 将字符串类型转成实际的数据类型，字际的数据类型是字典

# 获取字典中所有的key，转成列表类型
lst_title=list(d.keys())  # d.keys() 字典对象的方法

# 获取字典中所有的value，转成列表类型
lst_content=list(d.values())

# print(lst_title)
# print(lst_content)

lst=[lst_title,lst_content]   # 构造二维列表

wb=openpyxl.Workbook()    # 创建Excel工作簿对象
sheet=wb.active          # 获取当前的工作表对象(Sheet1)
for item in lst:        # 遍历列表 [['name','age'],['张三',20]]
    sheet.append(item)
wb.save('a.xlsx')     # 保存工作簿对象


# Python 操作XML
doc=Document()  # 创建文档对象


root =doc.createElement('student')   # 在文档对象中添加元素  ，元素的名称叫student
doc.appendChild(root) # 文件上添加根 ,添加子元素

nametag=doc.createElement(lst_title[0])  #  在文档对象中添加元素， 元素的名称是lst_title[0] name
nametag.appendChild(doc.createTextNode(lst_content[0])) # 向name中添加文本内容
root.appendChild(nametag) # name添加到根元素上


agetag=doc.createElement(lst_title[1]) # 在文档对象中添加元素，元素的名称是 age
                                     # str(lst_content[1])把20转成字符串类型
agetag.appendChild(doc.createTextNode(str(lst_content[1])))  # 向age中添加文本内容
root.appendChild(agetag)

# 创建文件 ，覆盖写
file =open('a.xml','w',encoding='utf-8')   #
# 文档对象的写入方法
doc.writexml(file,indent='\t',newl='\n',addindent='\t',encoding='utf-8')

file.close()

# xml文件的作用是用于存储数据