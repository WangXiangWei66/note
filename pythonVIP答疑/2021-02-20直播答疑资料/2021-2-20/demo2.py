# 教育机构：马士兵教育
# 讲    师：杨淑娟
# Python从Mysql数据库中查询出来的数据，绝对是列表
# lst相当于MySql数据库中一个3行4列的表格
lst=[
    ['1001','张三','100','98'],
    ['1002','李四','96','45'],
    ['1003','王五','45','100']
]
# csv文件的意思是逗号分隔值      1001，张三,100，98

file=open('a.csv','w',encoding='utf-8') #  a.csv文件的编程格式
for item in lst: # item就是一个小列表 表示的是一行数据
    # ','.join(item)表示的是列表中的元素使用逗号进行连接，结果是一个字符串类型
    file.write(','.join(item)+'\n')  #\n的意思是换行

file.close()
print('-------------------读取CSV文件内容----------------------------------')
fread=open('a.csv','r',encoding='utf-8')
s=fread.readlines() #读取全部内容
new_lst=[]
for item in s:
    item=item.strip('\n') #去掉\n
    r_lst=item.split(',') #按照逗号分隔，结果是一个列表
    new_lst.append(r_lst)
print(new_lst)
fread.close()