# 开发人员：刘健
# 开发时间：2022/4/25 0025 22:16

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    # 实例方法reverseList 转换列表 ,该 方法需要一个ListNode类型的参数
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

#[1,2,3,4,5]
        #  Solution()创建 Solution的对象    ， 相当于对象名.方法名()
        # 创建对象并调用方法
# result = Solution().reverseList([1,2,3,4,5])
# print(result)

s=Solution()  # 创建对象

#    请问[1,2,3,4,5]是ListNode类型吗？不是，所以30行代码的参数传递错误

#result=s.reverseList([1,2,3,4,5])  # 对象名.方法名()
# 以上两句代码与Solution().reverseList([1,2,3,4,5])功能相同
#print(result)

# 怎么改呢？
lst_node=ListNode([1,2,3,4,5]) # 创建ListNode类型的对象

result=s.reverseList(lst_node)
print(result)
