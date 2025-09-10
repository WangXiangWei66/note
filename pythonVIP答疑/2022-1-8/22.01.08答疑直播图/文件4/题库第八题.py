#题目018：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a=int(input('请输入余数a='))
b=int(input('请输入相加数字的个数:'))
s=0 #和
c=1 #正实数
d=1 #次幂
while c<10**b:
    arr=[]
    if c==a:#c是个位数
      arr.append(c)
      c=c+1
    elif d<b:#c不是个位数
        while d<b:
            if c%10**d==a:
                arr.append(c)
                d=d+1
        c=c+1

i=0
while i>=0:
    s=s+arr[i]
    i+=1
print(s)
