# coding:utf-8
# author:杨淑娟
year=[82,88,98,86,92,00,99]
print('原列表:',year)
# 遍历
for index,value in enumerate(year,start=10):  # index默认从0开始 ,index是一个变量名称，可以自定义,start称为起始序号
    print('index=',index,'value=',value)
    # if str(value)!='0':
    #     year[index]=int('19'+str(value))
    # else:
    #     year[index]=int('200'+str(value))
year.sort()
print(year)

# 如果一个函数不会使用了怎么办？按住ctrl键再去点击函数名称，进入到函数的定义处，可以看源代码
# 一个函数如何使用，就是看参数的传递