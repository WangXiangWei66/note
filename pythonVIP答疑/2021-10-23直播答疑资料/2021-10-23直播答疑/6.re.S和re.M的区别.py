# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#re.S单行匹配，re.M多行匹配
import  re
s='''love me
love you 
love her
welcome to beijing
beijing love you
'''
#pattern=re.compile('^love',re.S)  # 构建正则表达式的提取规则,# 只匹配第一行
pattern=re.compile('^love',re.M)  # 构建正则表达式的提取规则,#
lst=pattern.findall(s)
print(lst)

