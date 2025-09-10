# 教育机构：马士兵教育
# 讲    师：杨淑娟
# 希望在calc.py文件中导入demo.py    一个以.py结尾的文件就是一个模块
import  demo

#demo --》 代码
# 猜数游戏    ，使用False 表示猜对了，  使用True表示没猜对
import  random
num=random.randint(1,10)
print('--------------',num)
guess=eval(input('你猜啊?'))

a=False  #表示猜对了
if num!=guess:  #两个数不相等，表示没猜对
    a=True

if a:
    print('没猜对')
else:
    print('猜对了')






