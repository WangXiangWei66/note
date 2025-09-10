#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import urllib.parse
#https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%A9%AC%E5%A3%AB%E5%85%B5&fenlei=256&rsv_pq=9fc8819c000131ce&rsv_t=895fkvxFXCrFRlZU9lgjILFSSoJD2Nxmsk2A%2B20KJKTcTdeXR4QsY6TCHCc&rqlang=cn&rsv_enter=1&rsv_dl=ib&rsv_sug3=8&rsv_sug1=7&rsv_sug7=101
s='%E9%A9%AC%E5%A3%AB%E5%85%B5'
# 解码
ss=urllib.parse.unquote(s) #对ｓ进行解码
print(ss)

# 编码
print(urllib.parse.quote(ss))

# urllib.parse.unquote() 对中文进行解码（地址栏中的中文）
# urllib.parse.quote()对中文进行编码（编码之后的结果可以直接放到地址栏中）
# coding:   写在python文件的第一行，用于确定python文件的编码格式
# encoding:  是open方法的参数，用于确定打开文件的编码格式
with open('a.txt','w',encoding='utf-8') as file:
    file.write('中国')
