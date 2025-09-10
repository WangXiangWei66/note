#教育机构 ：马士兵教育
#讲    师：杨淑娟
# 爬虫程序
#(1)导入第三方模块  requests
import  requests
import  json
resp=requests.get('https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100006736466&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
#print(resp.text) #使用到response对象 的 text属性
#执行一个替换工作，目的时转成dict类型
content=resp.text.replace('fetchJSON_comment98(','').replace(');','')  #结果依然是一个字符串
#需要将字符串转成json格式  （将字符串转成字典类型）
json_data=json.loads(content)  #json_data就是一个变量而已，这个变量由两个单词组成，所以使用_进行连接
#print(type(json_data)) #type这个函数的作用，用于查看对象的数据类型 ,<class 'dict'>
#既然是字典就可以根据key获取值
comments=json_data['comments']   #[]与()什么时候用，()表示方法的定义或调用,[]表示列表的定义，字典的取值，列表的取值等操作
#print(type(comments)) #<class 'list'> 结果为列表类型  表示的是评论页的列表
#既然是列表，就可以使用for ..in进行遍历
for index,item in zip(range(1,len(comments)+1),comments):  #item表示的是列表中的每一个评论数据
   # print(type(item))  #列表中的每一个元素又是一个字典类型  ,再继续根据键获取值
    content=item['content']
    print(index,'-->',content)










