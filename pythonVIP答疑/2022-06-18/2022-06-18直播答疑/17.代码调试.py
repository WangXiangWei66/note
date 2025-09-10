# coding:utf-8
# author:杨淑娟
import random
words=["python","game","food","easy","number","integer"]
flag1=True

while flag1:
    word=random.choice(words)
    # s列表存贮打乱后单词的index
    s=[]
    while len(s)<len(word):
        value=random.randint(0,len(word)-1)
        # 保证s里的索引不会重复
        if value not in s:
            s.append(value)
    # 乱序单词
    wrong_word=""
    # 拼接
    for i in s:
        wrong_word+=word[i:i+1]
    # print(wrong_word)
    while True:
        print("单词已生成：",wrong_word)
        guess=input("请输入你心里想的那个单词：")
        if guess==word:
            fun=input("恭喜，猜对了！！ 要继续么（y/n）")
            if fun=="n" or fun=="N":
                flag1=False    # -->控制是while flag1
                break    # 不想继续了，退出循环，没有break是退不了循环  控制提while True ，只有退出while True ,才能继续退出while flag1
            else:
                break
        else:
            print("不对，请重猜.......")
