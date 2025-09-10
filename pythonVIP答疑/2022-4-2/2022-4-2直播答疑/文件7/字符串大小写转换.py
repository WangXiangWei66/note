#姓名：      安  鑫
#开发时间： 2022/3/29  23:12
#使用upper将所有字符转换为大写，产生一个新的对象
s='hello,python'
a=s.upper()
print(a,id(a))
print(s,id(s))
#使用lower()将所有字母转换为小写
print('-----------------------------------------------')
print(s,id(s.lower()))
print(s.lower(),id(s.lower()))
print(s.lower(),id(s.lower()))
print(s,id(s.lower()))
print('-----------------------------------------------')
print(s,id(s.lower()))
print(s.lower(),id(s.lower()))
print(s.lower(),id(s.lower()))
print(s,id(s.lower()))
print('--------------------------------------------------')
print(s,id(s.lower()))
print(s,id(s.lower()))
print(s,id(s.lower()))
print(s,id(s.lower()))
print(s,id(s.lower()))
print(s,id(s.lower()))
print(s,id(s.lower()))
print(s,id(s.lower()))
print('-------------使用swapcase()将大写字母转换为小写，小写字母转换为大写----------')
c='hello,Python,QEEn'
print(c.swapcase())

print('-----------使用capitalize()将第一个字符转换为大写，其余转换为小写-------------')
print(c.capitalize())
print('-------------使用title()将每个单词的第一个字母转换为大写---------------')
print(c.title())
