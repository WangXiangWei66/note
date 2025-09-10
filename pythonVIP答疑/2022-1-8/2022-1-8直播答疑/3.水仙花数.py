# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

def flower():
    lst=[]
    for i in range(100,1000):   #三位数才是水仙花数
        ge=i%10
        shi=i//10%10
        bai=i//100  #//表示整除    //在Java中是单行注释
        if ge*ge*ge+shi*shi*shi+bai*bai*bai==i:   #== 在Python中叫等值判断
            lst.append(i)
    return  lst

print(flower()) #3*3*3=27  7*7*7=343    1*1*1=1     27+343+1=371


def flower2():
    lst2=[]
    for i in range(100,1000):
        lst=list(str(i))  # 列表不需要反转 ,
        result =0
        for item in lst:
           result+= int(item)*int(item)*int(item)

        if result==i:
            lst2.append(i)
    return lst2
print(flower2())