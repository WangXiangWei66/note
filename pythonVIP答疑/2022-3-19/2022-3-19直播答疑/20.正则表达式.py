# coding:utf-8
# author:杨淑娟
import  re

s='<div>test1</div>bb<div>test2</div>cc'
# 贪婪模式
x=re.match('<div>.*</div>',s)
print(x.group())

# 非贪婪模式
x=re.match('<div>.*?</div>',s)
print(x.group())