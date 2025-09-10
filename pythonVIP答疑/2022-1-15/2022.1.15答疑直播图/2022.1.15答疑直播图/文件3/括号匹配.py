def valid_str(string):
    if len(string) % 2 ==1:
        return False
    stack=[]
    char_dic={")":"(","}":"{","]":"["}
    for char in string:
        if char in char_dic:
            if not stack or char_dic[char]!=stack.pop():
                return  False
        else:
            stack.append(char)
    return not stack

st="{}()[]"
st1="}{][)("
st2="{([)}]"
print(valid_str(st))
print(valid_str(st1))
print(valid_str(st2))