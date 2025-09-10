# 开发人员：刘健
# 开发时间：2022/4/25 0025 22:16

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

# [1,2,3,4,5]
result = Solution().reverseList([1,2,3,4,5])
print(result)