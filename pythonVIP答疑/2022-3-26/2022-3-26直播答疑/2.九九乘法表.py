# coding:utf-8
# author:杨淑娟
for i in range(1,9):
    for j in range(1,i+1):
        print(i,'*','=',i*j,end='\t')
    print()
print('---------------------')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()