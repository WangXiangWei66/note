#coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import jmespath # 这是一个第三方模块，作用是用地解析json
source={'a':'abc','b':'bcd','c':'cde'}
result=jmespath.search('a',source) # 单个查找，'a'这个键所对应的值
print(result)
# 常规的字典取值方式
print(source['a'])
print(source.get('a'))
# 层级查找

d={'a':
       {'b':
            {'c':
                 {
                     'd':'value'
                 }}}}

# 想要获取key为c的值
print(d['a']['b']['c'])
print(d.get('a').get('b').get('c'))
# 使用第三方模块  . 表示的是层次关系
result=jmespath.search('a.b.c',d)
print(result)

# 多表达式的综合使用
d={'a':
       {
           'b':{
               'c':[
                   {'d':[0,[1,2]]},
                   {'d':[3,4]}
               ]
           }
       }}  # 分行写的目的让大家看得清楚

#　d 中的1怎么获取
print(d['a']['b']['c'][0]['d'][1][0])  #看得懂吗？
print(d.get('a').get('b').get('c')[0].get('d')[1][0])

# 使用第三方模块
print(jmespath.search('a.b.c[0].d[1][0]',d))

print('--------------------实际应用中怎么中--------------------')