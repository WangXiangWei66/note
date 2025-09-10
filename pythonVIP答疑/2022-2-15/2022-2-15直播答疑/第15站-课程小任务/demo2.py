#coding=utf-8
#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/4/5 13:34
#任务2：模拟淘宝客服自动回复
def find_answer(question):
    with open('replay.txt', 'r',encoding='gbk') as file:
        while True:
            line = file.readline()  # 每次读取一行,读到文件末尾为空字符串
            if not line:  # 文件末尾刚退出循环
                break
            # 字符串的分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in question:
               return reply
    return False
#输入问题
question=input('Hi,xxx,你好，小蜜在此等主人很久了，有什么烦恼快和小蜜说说吧~')
#输入的问题在文件中是否有相应的回复内容
while True:
    if question=='bye':
        break
    #开始查找
    reply=find_answer(question)
    if not reply:
        question = input('小蜜不知道您在说什么，您可以问一些关于订单，支付，物流的相关问题（退出请输入bye）')
    else:
        print(reply)
        question = input('小主，您可以问一些关于订单，支付，物流的相关问题（退出请输入bye）')
print('小主再见')
