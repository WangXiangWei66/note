# coding:utf-8
# author:杨淑娟
#调用random模块，time模块，
import time
import random
#随机生成数字100~~150代表血量
print('【玩家】')
hp = random .randint (100,150)
print('【血量】',hp)
#随机生成30~~50代表攻击力
atk = random .randint(30,50)
print('【攻击】',atk)
time.sleep(1.5)
print('______________________')
print('【敌人】')
hp1 = random .randint (100,150)
print('【血量】',hp1)
atk1 = random .randint(30,50)
-0
print('【攻击】',atk1)
time.sleep(1.5)
#开始循环步骤，不确定次数用while循环
while True:
#，【玩家】剩余血量=玩家当前血量-敌人攻击。
    if hp1<=0 or hp<=0:
        break   # 当双向血量有一个为0时，退出循环
    else:
        hp=hp-atk1
    #【敌人】剩余血量=敌人当前血量-玩家攻击
        hp1=hp1-atk
        print('你发起了攻击，【敌人】剩余血量'+str(hp1))
        time.sleep(1.5)
        print('敌人向你发起了攻击，【玩家】剩余血量'+str(hp))
        print('——————————————————————————-')
        time.sleep(1.5)
# 从循环中取出
# 退出循环，显示对战结果
if hp > hp1:
    print('敌人死翘翘了，你赢了！')
elif hp < hp1:
    print('完蛋了，你被敌人击败了！')
else:
    print('棋逢对手，再战！！！')
