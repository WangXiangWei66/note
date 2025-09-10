def lengthOfLongestSubstring(s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):  # 取字符串中第i个字符为c
        if c in d:  # 如果c在字典里
            start = max(start, d[c] + 1)  # 将开始位置重新定位
        d[c] = i  # 记录 c 在字符串的最新位置
        ans = max(ans, i - start + 1)  # 记录最大不重复值
    return ans
n = lengthOfLongestSubstring('aacdefxabcdaaaadbdexxzzxcvsdfadsgfhgfh')
print(n)