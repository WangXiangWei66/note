# coding:utf-8
# author:杨淑娟

def solution(txt):
    s=set(txt.upper()) # 将字符串转成集合类型
    if len(txt)>len(s): # 说明有重复字符串
        return False
    else:
        return True

print(solution('Algorism'))
print(solution('PasSword'))
print(solution('Consecutive'))