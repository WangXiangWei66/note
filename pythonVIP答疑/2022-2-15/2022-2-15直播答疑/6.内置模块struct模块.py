# coding:utf-8
# author:杨淑娟
import struct
import binascii  # 包含很多二进制和ASCII的二进制表示转换的方法
values=(5,'hello'.encode('utf-8'),98.5) # 在元组中，有三个元素，三个元素对应3个不同的数据类型

#print(values,type(values))

# 写格式字符中，struct中的格式字符串
s=struct.Struct('I 5s f')
#print(s,type(s))

#对元组进行打包

packed_data=s.pack(*values) # 打包之后的数据
print(packed_data)#打包之后的数据
print(binascii.hexlify(packed_data)) # 数据的十六进制字符串


#可以进行解包

packed_data2=binascii.unhexlify(b'0500000068656c6c6f0000000000c542')
unpacked_data=s.unpack(packed_data2)
print(unpacked_data)


