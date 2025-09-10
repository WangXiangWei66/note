#创建一个列表，其中存储了3个Point对象。每个点（Point)都在与x,y轴夹角为45度的直线上（意思是x和y的值相同）。
# 打印输出这些点的坐标。如：p1(1,1) p2(2,2) p3(3,3)

#疑问：把def __new__(cls, *args)和其return语句进行注释之后，这段代码仍能正常运行，请问这两个语句在这段代码中的意义是什么？

#
class Point:
    equality = False
 
    # def __new__(cls, *args):    # 创建对象语句为系统 自动调用语句，无需手动调用
    #     return object.__new__(cls)
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x == y :
            self.equality = True
 
    def saveInfo(self):
        if self.equality:
            return self.x, self.y
        else:
            return None
 
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)
lst = [p1, p2, p3]
 
for p in lst:
    if p.equality:
        l = p.saveInfo()
        print(f"x坐标：{l[0]}，y坐标：{l[1]}")