# coding:utf-8
# author:杨淑娟
import re
tel_1='''
dadada
15811436234
12323131
wewerer
rewrwerwerwe
'''
telNo='15310823735'
                    #想表达3到9[3-9]
pattern=re.compile(r'1[5,9]\d{9}') # 以1开头第二位是3或者9，13或者19 ，将[3,9]改成[5,9]那么匹配的是15，或19

result=pattern.search(tel_1)
print(result)
print(pattern.match(telNo))

s='192.168.1.1'
p=re.compile('[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')

result=p.search(s)
print(result)

