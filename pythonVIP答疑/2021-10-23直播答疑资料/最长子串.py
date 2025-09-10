def lengthOfLongestSubstring(s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):  # ȡ�ַ����е�i���ַ�Ϊc
        if c in d:  # ���c���ֵ���
            start = max(start, d[c] + 1)  # ����ʼλ�����¶�λ
        d[c] = i  # ��¼ c ���ַ���������λ��
        ans = max(ans, i - start + 1)  # ��¼����ظ�ֵ
    return ans
n = lengthOfLongestSubstring('aacdefxabcdaaaadbdexxzzxcvsdfadsgfhgfh')
print(n)