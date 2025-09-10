# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 称编再解
import urllib.parse
s='杨淑娟'
ss=urllib.parse.quote(s) # 编码 ，可以在Url的地址栏中进行传输
print(ss)
# 解码
print(urllib.parse.unquote(ss))

# encoding 与coding的区别
# coding: 标识的是python文件的编码格式
# encoding  在open函数中使用过，可以是文本文件的编码格式
file =open('a.txt','w',encoding='utf-8')
file.close()

#urlencode，ensure_ascii
#urlencode 也是编码，对字典进行编码

d={'username':'杨淑娟','pwd':'88888'}
print(urllib.parse.urlencode(d)) #像是浏览器地址栏中参数的传输格式


# json格式转换时使用到过
import json   #想输出中时，指定的编码可行式
s=json.dumps(d,ensure_ascii=False) # 将字典类型转成字符串类型
print(s)  #
print(type(s))

# 与dumps对应的方法 是loads ()将字典型的字符串转成字典类型
dd=json.loads(s)

print(dd)
print(type(dd))

#
print("#"*4+'小吃....'+"*"*4)