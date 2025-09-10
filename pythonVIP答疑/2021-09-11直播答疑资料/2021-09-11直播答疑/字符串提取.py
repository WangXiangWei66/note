# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
name = ['show("3,14,21,45,46,9")', 'show("34")', 'xiao("4")', 'wu("4")', 'heshu("34")']
#解决方案，可以字符查找
for item in name:
    first=item.find('(')
    end=item.find(')')
    #字符串切片
    subst=item[first:end+1]
   # 使用eval去掉左右引号
    s=eval(subst)
    #print(s)
    # 字符串分割
    result=s.split(',')
    print(result)
