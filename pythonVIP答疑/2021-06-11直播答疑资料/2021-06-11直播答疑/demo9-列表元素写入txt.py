#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 假调这个内容就是函数的结果
def fun():
    lst=['FutureWarning 关于构造将来语义会有改变的警告',
    'OverflowWarning 旧的关于自动提升为长整型(long)的警告',
    'PendingDeprecationWarning 关于特性将会被废弃的警告',
    'RuntimeWarning 可疑的运行时行为(runtime behavior)的警告',
    'SyntaxWarning 可疑的语法的警告',
    'UserWarning 用户代码生成的警告']
    return lst

with open('a.txt','w',encoding='utf-8') as file : # 这个编码格式是a.txt文件的编码格式
    for item in fun():  # 调用函数fun()，结果为列表
        file.write(item+'\n')



