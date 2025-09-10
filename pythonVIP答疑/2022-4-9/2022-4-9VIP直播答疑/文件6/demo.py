# coding:utf-8
# author:杨淑娟
import sys

lst = []
init_allocated = sys.getsizeof(lst)  # 返回一个对象占用的内存, 以字节为单位的
#
# for i in range(1, 50):
#     lst.append(i)
#     now_allocated = sys.getsizeof(lst) - init_allocated
#     print(f'当前元素的数量:{i}, 当前的占用内存:{now_allocated}字节 当前的容量是:{now_allocated // 8}')

# print(sys.getsizeof('h'))
print(sys.getsizeof(1))
