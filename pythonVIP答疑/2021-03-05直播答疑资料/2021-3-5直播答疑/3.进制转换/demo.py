# 教育机构：马士兵教育
# 讲    师：杨淑娟
x=0xaa55
s=bin(x) #将x转成二进制 结果是str类型
print(s)
s=s[2:] # 把字符串中ob切掉了
print(s)
lst=[s[item:item+4] for item in range(0,len(s),4)]
print(lst)
for item in lst:
   s='0b'+item   #   '0b1010'
   print(eval(s))   # 0b1010
