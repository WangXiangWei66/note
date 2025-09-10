# coding:utf-8
# author:杨淑娟
lst=[11,22,33,44]
# 创建迭代器对象
ite=iter(lst)   # 使用列表创建迭代器对象，内置的函数iter()

print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
#print(next(ite))
print('-------------------------')
# 迭代对象可使用for循环遍历
ite= iter(lst)     # 多余不多余？  不多余 ，因为前边已经使用过next()遍历过所有的元素
for item in ite:
    print(item)


print('---------------------')
class MyNumbers(): # 自定义类   # 可不可以把self改成别的单词,可以，改成了ysj,程序员习惯上叫self
    def __iter__(ysj):    # 实现该 方法的目的是为了创建迭代器对象
        ysj.a=1  # 初始化实例属性
        return ysj  # 返回一个迭代器对象

    def __next__(ysj): # 实现该方法的目的是为了要从迭代器中取元素
        x=ysj.a
        ysj.a+=1
        return x  # 返回当前获取的元素

# 创建类MyNumbers的实例对象
num=MyNumbers()


# 创建迭代器对象
ite=iter(num)


print(next(ite)) # 通过next()获取迭代器中的元素
print(next(ite))
print(next(ite))

print()

