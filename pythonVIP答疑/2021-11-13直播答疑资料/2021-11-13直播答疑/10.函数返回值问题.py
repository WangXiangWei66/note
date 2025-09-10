# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

file=open('c.txt','a')
file.write('中国') # 该方法的返回值为int
print(file.write('中国') ) # 字符的个数

lst=['java','go','python']
file.writelines(lst) # 该方法没有返回值，所以输出结果为None
print(file.writelines(lst))
file.close()
