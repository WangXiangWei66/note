dic={'a':1,'b':2,'c':3}
#使用[]进行取值
print(dic['a']) #因为名称为 'a'的键在字典中存在
#print(dic['d']) #KeyError: 'd'  如果键不存在，程序报 错

print(dic.get('d'))  #'d'这个键在字典中不存， 返回 None
print(dic.get('d',4)) # 'd'这个键在字典中不存在时，则使用设置的默认值4进行显示
print(dic.get('a',100)) #因为'a'这个键在字典中，所以会获取实际值，默认值无效

print(dic)  #建议字典取值的使用get()方法
