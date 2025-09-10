# coding:utf-8
#开发时间：2020/4/5 13:34   第一个代码，确定的是demo1.py的编码格式
#任务2：模拟淘宝客服自动回复
def find_answer(question):
    with open('replay.txt', 'r',encoding='utf-8') as file:
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


'''
读别人的代码，不是从上往下读，而是先划程序结构
以上代码分四块
1.函数的定义
2.输入    --》首先输入
3.循环    --》其次执行while True ,当看到while True时，就会想到在循环中一定有一个if和break
         (return的使用位置时函数或方法，作用是结束函数或方法)
          19行--》判断question=='bye' ,该判断是循环结束条件，当输入的值为bye里循环结束
          当输question的值不是bye时执行22行
          22 --》为函数的调用--》会到函数的定义处，函数的定义处为第3行
          3行--》进行入函数体
          4行--》打开一个文本文件
          5行--》while True ，可以猜想出，循环中一定有一个if..break用于退出循环
          6行--》从文件中读了一行数据，结果是一个字符串
               line= '订单|如果您有任何订单问题，可以登录淘宝账号，点击“我的订单”，查看订单详情'
          7行-->判断是否到文件尾 if  not line 
               每个对象都有一个布尔值 ，空字符串的布尔值为False，非空字符串的布尔值为True
                循环第一次读取   line的布尔值为True   if not True  结果为False，条件不成立，执行10行
         10行11行--》分割读取内容，分成两段，第一段的索引为0 , ‘订单’，第二段的索引为1，‘如果您有任何订单问题，可以登录淘宝账号，点击“我的订单”，查看订单详情’
         12行--》使用到一个in关键， X 是否在 Y中 
                   ‘订单’ 是否在 输入的内容里 question中
                     在    ： 结束函数，返回  回复内容 （回复内容就是第二段）
                     不在  ：循环继续
         5--》6--》7--》10--》11--》12  不在
         5--？6--》7--》10--》11--》12   不在
         5--》6--》7-》10-》11--》12   不在
         5-->while True  6-->readline()-->-7-->if not line  结果为True，因为读到空符串了
         --》8break退出循环  ，执行第14句，  return False  结束函数
         回到22行  reply这个变量的值有两种情况
            1）回复内容，是一个字符串    if  ..in  question 为True时
            2） False， 是一个布尔类型    文件读到最后
         23行  判断 reply的值
             if not reply  :   判断的结果为两种情况（两种可能性）
             1）reply得到是回复内容  reply的布尔值为True 那么 not True ，就会执行else进入到26，27行
             2）reply得到是False ， not False ，结果为True，执行if 进入到24行， 
                question=input(.....)重新输入内容
            当question的值为bye时整个程序结束
             
         
4.打印输出--》程序最后执行（当循环执行结束最后执行输出）
'''
# 基础语法建议不低于3遍
# 一段代码反复敲，找灵感  ，宁愿一段代码敲10次，也不要10段代码每个敲1次
# 算法与 Python语法无法，  算法是问题的解决方案，这个方案可以使用java代码实现，可以使用python代码实现
# 语法  ：分支，循环，列表，集合，元组，字典，函数，类和对象，文件读写


