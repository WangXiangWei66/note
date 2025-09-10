# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
word='当下两军相对，左有云长，右有....云长舞动大刀...被云长刀起...'
name='云长翼德'  # name[0:2] 切片，切出来的结果 是  “云长”
count=word.count(name[0:2]) # 统计"云长"出现的次数

#print(count) # 一共出现了3次
order='' # 用于连接出现的位置
size=-2 # 为什么要用size=-2，因为 要查询数据， 内容的长度为2

for i in range(count): #循环执行三次
     # find的方法的作用是查询 find(查谁，从哪开始查），查到的结果是多少，只返加第一个的索引
    size=word.find(name[0:2],size+len(name[0:2])) # 第一次从0开始查找 ,第二次从11开始，
                             #第一次循环 -2+2=0 word.find('云长',0)从索引为0的位置开始查  结果为9 size的值为9
                             # 第二次循环9+2 word.find('云长',11)
                             # 第三次循环 18+2  word.find('云长',20)

    print(size)


