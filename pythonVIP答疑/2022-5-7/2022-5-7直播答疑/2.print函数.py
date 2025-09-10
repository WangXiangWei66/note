# coding:utf-8
# author:杨淑娟
print('hello','world')  # 个数可变的位置参数 ，中间使用逗号分隔
print('hello'+'world') # 字符串的拼接操作

# 查看源代码，  按键 盘上的ctrl+点print函数
# def print(self, *args, sep=' ', end='\n', file=None):
'''
  *args ，个数可变的位置参数
  sep=' ' ，默认值参数，个数可变的位置参数在进行输出时，两者之间会有一个空格
  end='\n' ,默认值参数，默认输出之后会进行换行
  file=None，默认值参数， 用于使用print函数向文件中输出信息时使用
'''
# 以下两句代码的运行效果完全相同
print('hello','wolrd',sep='') # 分隔符设置为一个空字符串，即可
print('hello'+'world')