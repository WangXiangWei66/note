from functools import reduce
Tn=0
Sn=[]
n=int(input('n='))
a=int(input('a='))
for j in range(n):
    Tn=Tn+a
    a=a*10
    Sn.append(Tn)
    print(Tn)
S=reduce(lambda x,y:x+y,Sn)
print(S)