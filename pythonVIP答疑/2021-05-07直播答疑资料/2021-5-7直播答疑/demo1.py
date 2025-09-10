# 教育机构：马士兵教育
# 讲    师：杨淑娟
# apply函数，map函数，applymap函数
# 数据分析第三方模块pandas
#(1)apply函数，对行或者列进行操作，可应用的对象为DataFrame和Series
import pandas as pd
# 在Python中一切皆对象，创建Series对象 （相当于一个一组数据）
s=pd.Series(data=[10,20,30,40],index=['a','b','c','d']) # data称为关键字参数
print(s)
# apply这个函数本身就是用于执行函数
s=s.apply(lambda x:x+10)  # 对s中每一个元素都执行一次 apply()小括号中的函数
print(s)

# 对DataFrame中的行 或者列应用 函数 DataFrame相当于二维表格，有行索引还有列索引
df=pd.DataFrame(data=[[10,20,30,40],[11,22,33,44]],index=['a','b'],columns=['A','B','C','D'])
print(df)

# 对行执行某个函数
df2=df.apply(lambda x:x.sum(),axis=0)  #对行求行　
print(df2)

df2=df.apply(lambda x:x.sum(),axis=1)  #对列求行　
print(df2)


# map()只能在Series中上使用 ,map()这个函数的作用是对Series中的每个元素执行某个函数
s=pd.Series(data=[10,20,30,40],index=['a','b','c','d'])
print(s)

# fun函数的作用，判断传入的参数是一个大于20还是小于等于20的数
def fun(d):
    if d>20:
        return '大于20'
    else:
        return '小于等于20'


ss=s.map(fun)  # map是Series对象的方法
print(ss)

# applymap()是DataFrame的方法，对DataFrame中的每个元素都执行一次函数
print('---------------------------------')
df=pd.DataFrame(data=[[10,20,30,40],[11,22,33,44]],index=['a','b'],columns=['A','B','C','D'])
print(df)
df3=df.applymap(fun) #DataFrame中的每个元素都做为fun方法中的参数进行传递
print(df3)

# map是Series对象的方法
# applymap是DataFrame对象的方法
#apply即是Series对象的方法也是DataFrame对象的方法
