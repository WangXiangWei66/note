#题目019：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
x=1
a=0
y=0
while 0<x<=1000:
   for i in range(1,x+1):
       if x%i==0:
           y=y+i
           i=i+1
           if x==y:
               a=a+1
               print(x)
   else:
       x=x+1
   continue
def i():
    for m in (2,i):
        if i%m!=0:
            return i


