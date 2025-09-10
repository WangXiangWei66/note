#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# XML ：可扩展标记语言，存储和传输数据使用,使用的是自定义标签
# HTML :超文件标记语言，展示数据，使用的是因定标签 <h1><p>....

# 使用Python解析XML文件
'''
 (1)SAX,采用的是流的方式读取XML文件，占用内存空间比较小，速度也比较快，实现回调函数handler
 (2)DOM :将XML映射到内存中树，速度比较慢，占用内存空间大
 (3)ElementTree(元素树) ，相当于轻量级的DOM，点用内存小，速度快
'''
# 安装第三方模块xml
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 调用parse方法，返回解析树
tree=ET.parse('movies.xml')

# 获取根节点
root=tree.getroot()
#print(root.tag,root.attrib) # 输出根节点的名称，和根节点的属性

# 遍历root下的4个节点
for child in root:
   # print(child.tag,child.attrib) # movie节点
    for subchild in child:
        print(subchild.tag,subchild.text) # 节点名称，节点中的文本
    print('--------------------------')

# 对XML文件添加元素 （在root下添加子元素）
# 创建一个元素对象
ele=ET.SubElement(root,'movie')  # 在root--colletion下创建一个movie的标签
ele_type=ET.SubElement(ele,'type') # movie,xml中一个标签的名称
ele_format=ET.SubElement(ele,'format')
ele_year=ET.SubElement(ele,'year')
ele_rating=ET.SubElement(ele,'rating')
ele_stars=ET.SubElement(ele,'stars')
ele_description=ET.SubElement(ele,'description')
# 为标签添加文本
ele_type.text='1111'
ele_format.text='2222'
ele_year.text='3333'
ele_rating.text='4444'
ele_stars.text='5555'
ele_description.text='6666'

# 保存到xml文件中
#tree.write('movie.xml',encoding='utf-8',xml_declaration=True)
# 带格式的保存
def saveXML(root,filename,indent='\t',newl='\n',encoding='utf-8'):
    rawText=ET.tostring(root)
    dom=minidom.parseString(rawText)
    with open(filename,'w') as file:
        dom.writexml(file,'',indent,newl,encoding)


# 删除使用remove
for child in root:
    for sub in child:
        if sub.tag=='stars': #把所有的 stars标签都删除
            child.remove(sub) # remove删除的是子元素

# 调用保存
saveXML(root,'m.xml')





