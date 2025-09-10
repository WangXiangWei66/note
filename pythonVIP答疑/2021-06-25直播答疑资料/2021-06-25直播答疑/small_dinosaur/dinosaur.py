#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/5/2 22:56
import pygame                         # 将pygame库导入到Python程序中
from pygame.locals import  *          #导入pygame中的常量
SCREENWIDTH=822                       #窗体宽度
SCREENHEIGHT=260                      #窗体高度
FPS=30



#更新画面的时间

def game_over():
    bump_audio=pygame.mixer.Sound('audio/bump.wav')#撞击
    bump_audio.play()   #播入撞击音效
    #获取窗体高度与宽度
    screen_w=pygame.display.Info().current_w
    screen_h=pygame.display.Info().current_h
    #加载游戏结束的图片
    over_img=pygame.image.load('image/gameover.gif').convert_alpha()
    #将游戏结束的图片绘制在窗体的中间位置
    SCREEN.blit(over_img,((screen_w-over_img.get_width())/2,(screen_h-over_img.get_height())/2))

def mainGame():
    score=0                           #得分
    over=False
    global SCREEN,FPSCLOCL
    pygame.init()                    #初始化pyage
    #使用pygame时钟之前，必须先创建Clock对象的一个实例
    #控制每个循环多长时间运行一次
    FPSCLOCL=pygame.time.Clock()
    #创建一个窗体，方便我们与程序的交互
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('小恐龙')    #设置窗体标题

    #创建地图对象
    bg1=MyMap(0,0)
    bg2=MyMap(800,0)

    #创建恐龙对象
    dinosaur=Dinosaur()

    #添加障碍物的时间
    addObstacleTimer=0
    #障碍物对象列表
    lst=[]
    while True:
        # 判断是否单击了关闭窗体
        for event in pygame.event.get():
            # 如果单击了关闭窗体就将窗体关闭
            if event.type == QUIT:
                exit()  # 关闭窗体
            #单击键盘空格键，开启跳的状态
            if event.type==KEYDOWN and event.key==K_SPACE:
                if dinosaur.rect.y>=dinosaur.lowest_y: #如果恐龙在地面上
                    dinosaur.jump()                    #开启恐龙跳的状态
                    dinosaur.jump_audio.play()         #播放小恐龙跳跃音效

                     # 判断游戏结束的开关是否开启
                if over==True:
                    mainGame() #如果开启将调用mainGame()方法重新启动游戏

        #增加障碍物时间
        addObstacleTimer+=20
        pygame.display.update()  # 更新整个窗体
        FPSCLOCL.tick(FPS)  # 循环应该多长时间运行一次
        if over==False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()
            #恐龙移动
            dinosaur.move()
            dinosaur.draw_dinosaur()  #绘制恐龙

            #计算障碍物间隔时间
            if addObstacleTimer>=1300:
                r=random.randint(0,100)
                if r>40:
                    #创建障碍物对象
                     obstacle=Obstacle()
                    #将障碍物对象添加到列表中
                     lst.append(obstacle)
                #重置添加障碍物时间
                addObstacleTimer=0
                #循环遍历障碍物
            for i in range(len(lst)):
                lst[i].obstacle_move()
                lst[i].draw_obstacle()

                    # 判断小恐龙与障碍物是否碰撞
                if pygame.sprite.collide_rect(dinosaur, lst[i]):

                     over = True  # 撞击后开启结束开关
                     game_over()  # 调用游戏结束的方法

                else:

                        # 判断小恐龙是否跃过了障碍物
                     if (lst[i].rect.x + lst[i].rect.width) < dinosaur.rect.x:
                            # 加分
                         score += lst[i].getScore()

                    # 显示分数
                lst[i].showScore(score)



#定义一个滚动地图类
class MyMap():
    def __init__(self,x,y):
        #加载背景图片
        self.bg=pygame.image.load('image/map1.jpg').convert_alpha()
        self.x=x
        self.y=y

    #地图滚动的方法
    def map_rolling(self):
        if self.x<-790:          #小于-790说明地图已经移动完毕
            self.x=800           #给地图一个新的坐标点
        else:
            self.x-=5           #5个像素向左移动

    #无限滚动的方法
    def map_update(self):
        SCREEN.blit(self.bg,(self.x,self.y))


from itertools import cycle #导入迭代工具
#恐龙类
class Dinosaur():
    def __init__(self):
        #初始小恐龙矩形
        self.rect=pygame.Rect(0,0,0,0)
        self.jumpState=False  #跳跃的状态
        self.jumpHeight=130   #跳跃的高度
        self.lowest_y=140     #最低坐标
        self.jumpValue=0      #跳跃增变量

        #小恐龙动图索引
        self.dinosaurIndex=0
        self.dinosaurIndexGen=cycle([0,1,2])

        #加载小恐龙图片
        self.dinosaur_img=(
            pygame.image.load('image/dinosaur1.gif').convert_alpha(),
            pygame.image.load('image/dinosaur2.gif').convert_alpha(),
            pygame.image.load('image/dinosaur3.gif').convert_alpha()
        )
        self.jump_audio=pygame.mixer.Sound('audio/jump.wav') #跳
        self.rect.size=self.dinosaur_img[0].get_size()
        self.x=50       #绘制恐龙的x坐标
        self.y=self.lowest_y  #绘制恐龙的y坐标
        self.rect.topleft=(self.x,self.y)

    #跳状态
    def jump(self):
        self.jumpState=True

    #小恐龙移动
    def move(self):
        if self.jumpState:               #当起跳的时候
            if self.rect.y>=self.lowest_y:#站在地上
                self.jumpValue=-10        #以5个像素向上移动
            if self.rect.y<=self.lowest_y-self.jumpHeight:#恐龙到达顶部回落
                self.jumpValue=5   #以5个像素向下移动
            self.rect.y+=self.jumpValue     #通过循环改变恐龙y轴的坐标
            if self.rect.y>=self.lowest_y: #如果恐龙回到地面
                self.jumpState=False       # 关闭跳跃状态
    #绘制恐龙
    def draw_dinosaur(self):
        #匹配恐龙动图
        dinosaurIndex=next(self.dinosaurIndexGen)
        #绘制小恐龙
        SCREEN.blit(self.dinosaur_img[dinosaurIndex],(self.x,self.rect.y))

import random
#障碍物类
class Obstacle():
    score=1
    def __init__(self):
        #初始化障碍物矩形
        self.rect=pygame.Rect(0,0,0,0)
        #加载障碍物图片
        self.stone=pygame.image.load('image/stone.gif').convert_alpha()
        self.cacti=pygame.image.load('image/cacti.gif').convert_alpha()
        #加载分数图片
        self.numbers=(pygame.image.load('image/0.gif').convert_alpha(),
                      pygame.image.load('image/1.gif').convert_alpha(),
                      pygame.image.load('image/2.gif').convert_alpha(),
                      pygame.image.load('image/3.gif').convert_alpha(),
                      pygame.image.load('image/4.gif').convert_alpha(),
                      pygame.image.load('image/5.gif').convert_alpha(),
                      pygame.image.load('image/6.gif').convert_alpha(),
                      pygame.image.load('image/7.gif').convert_alpha(),
                      pygame.image.load('image/8.gif').convert_alpha(),
                      pygame.image.load('image/9.gif').convert_alpha())

        #加载加分音效
        self.score_audio=pygame.mixer.Sound('audio/score.wav')
        #产生0到1的随机数
        r=random.randint(0,1)
        if r==0:  #如果随机数为0显示石头障碍物相反显示仙人掌
            self.image=self.stone
        else:
            self.image=self.cacti

        #根据障碍物的宽高来设置矩形
        self.rect.size=self.image.get_size()
        #获取位图宽高
        self.width,self.height=self.rect.size

        #障碍物绘制坐标
        self.x=800
        self.y=200-(self.height/8)
        self.rect.center=(self.x,self.y)

    #障碍物移动
    def obstacle_move(self):
        self.rect.x-=5

    #绘制障碍物
    def draw_obstacle(self):
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

    #获取分数
    def getScore(self):
        self.score
        tmp=self.score
        if tmp==1:
            self.score_audio.play()
        self.score=0
        return  tmp

    #显示分数
    def showScore(self,score):
      '''在窗体中间的位置显示分数'''
      self.scoreDigits=[int(x) for x in list(str(score))]
      totalWidth=0
      for digit in self.scoreDigits:
          #获取积分图片的宽度
          totalWidth+=self.numbers[digit].get_width()
          #分数横向位置
      Xoffset=(SCREENWIDTH-totalWidth)/2
      for digit in self.scoreDigits:
          #绘制分数
         SCREEN.blit(self.numbers[digit],(Xoffset,SCREENHEIGHT*0.1))
         #随着数字增加改变位置
         Xoffset+=self.numbers[digit].get_width()

if __name__ == '__main__':
    mainGame()

#