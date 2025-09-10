# coding:utf-8
# author:杨淑娟
s='runoob\t12345\tabc'
print('原始字符串:',s)
print(r'替换\t符号:',s.expandtabs(8)) #tabsize默认为8
print(r'替换\t符号:',s.expandtabs(10))
