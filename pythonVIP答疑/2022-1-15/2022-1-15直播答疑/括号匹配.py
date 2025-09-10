def valid_str(string):
    if len(string) % 2 ==1:
        return False
    stack=[]
    char_dic={")":"(","}":"{","]":"["}
    for char in string:
        if char in char_dic:
            # 空列表布尔值为False ，非空列表的布尔值 为True
            if not stack or char_dic[char]!=stack.pop(): # 默认移除最后一个元素
                return  False
        else:
            stack.append(char)
    return not stack

st="{}()[]"
st1="}{][)("
st2="{([)}]"
print(valid_str(st)) # 为什么是True  因为最后执行的是return not stack,而 stack是空，所以布尔值为False,not False，取反，结果为True
print(valid_str(st1)) # 为什么是False，因为 第9行 not stack的结果为True，所以if成立，执行第10行，return False函数 结束
print(valid_str(st2))