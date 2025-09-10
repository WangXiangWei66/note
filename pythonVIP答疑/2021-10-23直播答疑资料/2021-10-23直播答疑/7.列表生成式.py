# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
lst=[[i,i if i%2==0 else 20] for i in range(10)]
print(lst)

#如果if的判断条件为True  ，结果为[i,i]
# 如果条件为False，如果为 [i,20]  # 如果条件为False，将20赋值给第二个i
QualityPointSource = [{"q_point_source":"Zp8","q_point_nickname":""},{"q_point_source":"RoadTest","q_point_nickname":"路试"}]
qpoint = [[x["q_point_source"], x["q_point_nickname"] if x["q_point_nickname"] else x["q_point_source"]] for x in QualityPointSource]
print(qpoint) #[['Zp8', 'Zp8'], ['RoadTest', '路试']]

# 为什么会产生这种结果
'''
第一次遍历 结果为  {"q_point_source":"Zp8","q_point_nickname":""}
  if x["q_point_nickname"]  结果为False  ， x["q_point_nickname"] 字典取值，取出来的结果为""，空字符串的布尔值为False
  所以会执行else 部分
   x["q_point_source"] 结果为"Zp8"
   将else部分的值赋给逗号之后的x["q_point_nickname"]  ,else部分取值结果为Zp8  ，所以
   相当于     x["q_point_nickname"]=x["q_point_source"]  赋值过值  x["q_point_source"]为Zp8
   所以第一遍历处理的结果为["Zp8","Zp8"]
第二次遍历 结果为   {"q_point_source":"RoadTest","q_point_nickname":"路试"}
  执行if判断  结果为True，执行if之前的内容
  x["q_point_source"], x["q_point_nickname"]  就是取值操作
  ["RoadTest","路试"]


'''