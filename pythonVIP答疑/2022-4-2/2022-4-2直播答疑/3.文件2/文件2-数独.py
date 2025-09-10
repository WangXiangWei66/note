# coding: utf-8

import math

class point:
    def __init__(self,x_pos,y_pos):
        self.x=x_pos
        self.y=y_pos
        # 可填写的数值
        self.available=[]
        # 数值
        self.value=0

# 取出行非零值
def row_judgement(point,lst):
    length = len(lst)
    n = int(math.sqrt(length))
    row=set(lst[point.y:point.y+n])
    row.remove(0)
    return row

# 取出列非零值
def col_judgement(point,lst):
    length = len(lst)
    col_lst=[]
    n = int(math.sqrt(length))
    for i in range(point.x,len(lst),n):
        col_lst.append(lst[i])
    col=set(col_lst)
    col.remove(0)
    return col

def initPos(ls):
    length=len(ls)
    p_lst=[]
    for i in range(length):
        if ls[i] == 0:
            # 需填写的元素下标
            p=point(i%int(math.sqrt(length)),i//int(math.sqrt(length)))
            # 该位置的可选值
            n=int(math.sqrt(length))
            for j in range(1,n+1):
                if j not in row_judgement(p,ls) and j not in col_judgement(p,ls):
                    p.available.append(j)
            p_lst.append(p)
    return p_lst

# 每一个点的填充数值
def fill_num(point,lst,pl):
    # 可能值
    all=point.available
    for item in all:
        point.value=item
        if check_data(point,lst):
            # 填值
            lst[point.y*4+point.x]=item
            # 正确数值
            if len(pl) ==0:
                # return
                disp(lst)
                exit(0)
            p2=pl.pop()
            fill_num(p2,lst,pl)
            # 回溯
            lst[point.y * 4 + point.x] =0
            lst[p2.y * 4 + p2.x] =0
            p2.value=0
            pl.append(p2)
        else:
            pass

# 核对数值
def check_data(point,ls):
    # if point.value==0:
    #     return  False
    if point.value not in row_judgement(point,ls) and point.value not in col_judgement(point,ls):
        return  True

def disp(lst):
    count=0
    for i in range(len(lst)):
        print(lst[i],end="  ")
        count+=1
        if count % math.sqrt(len(lst))==0:
            print()

if __name__ == '__main__':
    sudoku=[
        4,0,0,0,
        0,0,0,1,
        0,0,1,0,
        0,0,3,4
    ]
    disp(sudoku)
    # 每个point的可能值
    ps=initPos(sudoku)
    print()
    p=ps.pop(0)
    fill_num(p,sudoku,ps)

# 数独
#   1 2 3 4
#   2 3 4 1
#   3 4 1 2
#   4 1 2 3