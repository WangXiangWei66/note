# coding:utf-8
# author:杨淑娟
# -*- coding = utf-8 -*-
# @Time : 2021/12/11
# @Author :小吴
# @File :chop3.py
# @Software :PyCharm
'''
全局文本检索替换  #写完后的脚本调用方式# python your_script.py old_str new_str filename
'''
import sys
print(sys.argv)
old_sr=sys.argv[1]
new_sr=sys.argv[2]
fileuname=sys.argv[3]

fileuname=sys.argv[0]
# 1 load into ram
f=open(fileuname,'r+',encoding='utf-8')
data=f.read()
#  2 count and replace
old_sr_cunt=data.count(old_sr)
new_data=data.replace(old_sr,new_sr)
#  3 clear old fileuname
f.seek(0)
f.truncate()
# 4 保存 new data 到文件
f.write(new_data)
print(f"成功替换字符{old_sr}'to'{new_sr}',共{old_sr_cunt}处。。。")
