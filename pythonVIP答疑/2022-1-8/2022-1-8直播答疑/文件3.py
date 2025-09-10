# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#替换字符串中的问号
def fun(s):
    res = list(s)  # res中的值['?','d','s']
    n = len(res)  #  n=3
    for i in range(n):  # 循环3次，i的取值为 0,1,2
        if res[i] == '?':     #res[0]的值为？ 判断结果为True
            for b in "abc":   # 第一次循环时,b的变量的值是a
                       #0>0 为False  or  0<3-1 and res[0+1]=='a'  结果为False or False   not  False 结果为True
                if not (i > 0 and res[i - 1] == b or i < n - 1 and res[i + 1] == b):  #and优先级大于or
                    res[i] = b  # 执行里面的代码  res[0]='a' 这个时候  res的值为['a','d','s']
                    break  # 退出 内层for循环
    return ''.join(res)

print(fun('?ds'))
'''
第一次循环  res[0]=='?'结果为True，将执行里面的for
内层循环 
  第一次：  b的值为 'a'
      i的值为0  0>0 and res[0-1]=='a'的结果为False 
      0<3-1 and res[1]=='a' 结果为False    ，False or False结果为False  not False结果为True，执行里面赋值操作
      res[0]='a' 这里，res的内容为[a,d,s]
      break出循环
           res[1]的值是d
第二次循环 res[1]=='?'的结果为False，
        res[2]的值是s
第三次循环 res[2]=='?'的结果为False，
最后执行 ''.join([a,d,s])，最终结果为ads
                    
   
'''