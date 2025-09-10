# coding:utf-8
# author:杨淑娟
def diff_lst_float(start,end,n):
    start,end=float("%.3f" % start),float("%.3f" %  end)
    step=(end-start)/n
    # 处理初始值start
    # 字符串拼接
    start= str(start) + '00' if len(str(start).split('.')[1]) != 3 else start

    lst=[start]
    for i in range(1,int(end)):
        value=float(start)+step
        if value>end:
            break
        x=str(round(value, 3))  # 将float类型转成字符串类型
        # 字符串拼接
                     # 按照小数点进行分隔，小数点后面的字符串的长度！=3位
        x=x+'00'if len(x.split('.')[1])!=3 else x  # 转成字符串类型，小数点后不满足3位小数的使用0补齐

        lst.append(x)
        start=value
    print(lst)

#怎么设置使列表都是3位小数？
diff_lst_float(1,50,3)


# def diff_lst_float(start,end,n):
#     start,end=float("%.3f" % start),float("%.3f" %  end)
#     step=(end-start)/n
#     lst=[start]
#     for i in range(1,int(end)):
#         value=start+step
#         if value>end:
#             break
#         lst.append(round(value,3))  # round
#         start=value
#     print(lst)
#
# diff_lst_float(1,50,3)