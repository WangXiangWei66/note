#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  requests
resp=requests.get('https://club.jd.com/comment/productPageComments.action?productId=100001991065&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
#print(resp.text)
json_data=resp.json()
#print(type(json_data))
comments=json_data['comments']  #[]的使用 ，字典的取值 ,取出来之后，结果为list
#print(type(comments)) <class 'list'>，由于是列表，就需要遵照列表的取值方法
print('---------------------列表取值方式一------------------------')
for i in range(len(comments)):  #根据索引取值  i,表示的是索引
   # print(comments[i])
    print (comments[i]['content'])

print('----------------------列表取值方式二--------------------------')
for item in comments:   #item表示的是列表中的元素
    #print(item)    #comments[i]与item的含义是相同的  取取来的结果为 dict类型
    content=item['content']  #由于item 一个字典，继续遵循字典的取值方式
    print(content)






