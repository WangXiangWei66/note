class Node():
    def __init__(self,data):
        # 数据
        self.data=data
        # 节点
        self.pointer=None

# 循环链表
class LoopLinkList():
    # 头结点指向节点
    def __init__(self,Node=None):
        self.head=Node
        if Node:
            Node.pointer=Node

    def is_empty(self):
        if self.head==None:
            return True

    def get_length(self):
        if self.is_empty():
            print("空的单链表")
            return 0
        count=1
        current=self.head
        while current.pointer!=self.head:
            count+=1
            current=current.pointer
        return count

    def loop_list(self):
        if self.is_empty():
            return
        current = self.head
        while current.pointer!=self.head:
            print(current.data,end=", ")
            current=current.pointer
        print(current.data)
        print()

    def add_element(self,index,element):
        node=Node(element)
        # 头插法
        if index==1:
            # 空链表
            if self.is_empty():
                self.head=node
                node.pointer=node
            else:
                # 遍历
                current = self.head
                while current.pointer!=self.head:
                    current = current.pointer
                node.pointer=self.head
                self.head=node
                # 修改尾元素指向
                current.pointer=self.head
                print("元素头插法插入成功！")
        else:
            # 尾插法
            if index==-1:
                # 空链表
                if self.is_empty():
                    self.head = node
                    node.pointer = node
                else:
                    current=self.head
                    while current.pointer!=self.head:
                        current = current.pointer
                    current.pointer=node
                    node.pointer=self.head
                    print("元素尾插法插入成功！")
            else:
                # current = self.head
                current=self.head
                count=0
                while count<=index-1:
                    count+=1
                    # 插入位置的前一个节点
                    if count==index-1:
                        node.pointer=current.pointer
                        current.pointer=node
                        print("元素指定位置插入成功！！")
                        return


    def delete_element(self,element):
        current = self.head
        pre=None
        # 首元素
        if current.data==element:
            self.head=current.pointer
        else:
            while current.pointer!= self.head:
                if element==current.data:
                    pre.pointer=current.pointer
                    current.pointer=None
                    print("元素删除成功！")
                    return
                else:
                    pre=current
                    current=current.pointer
            else:
                # if current.pointer==self.head and current.data==element:
                #     current=self.head
                #     while current.pointer!=self.head:
                #         pre.pointer=current
                #         current=current.pointer
                #     pre.pointer=self.head
                #     current.pointer=None
                # else:
                    print("not found.......")

    def find_element(self,element):
        current=self.head
        while current.pointer!=self.head:
            if element==current.data:
                print("element found!!")
                return
            else:
                current=current.pointer
        else:
            print("element not found!!")

if __name__ == '__main__':
    n1=Node(100)
    lst=LoopLinkList(n1)
    lst.add_element(-1,200)
    lst.add_element(-1,400)
    lst.add_element(1,300)
    # print(lst.get_length())   4
    print("lst.add_element(2,800)")
    lst.add_element(2,800)
    print(lst.get_length())
    lst.loop_list()
    print("lst.add_element(3,100)")
    lst.add_element(3,700)
    lst.loop_list()
    print("*"*6)
    print("lst.delete_element(400)" )
    lst.delete_element(400)
    lst.loop_list()
    print("lst.delete_element(500)" )
    lst.delete_element(500)
    lst.loop_list()
    print("lst.delete_element(300)")
    lst.delete_element(300)
    lst.loop_list()
    print("lst.delete_element(100)")
    lst.delete_element(100)
    lst.loop_list()
    print("lst.find_element(200)")
    lst.find_element(200)
    print("*" * 6)
    print("lst.find_element(300)")
    lst.find_element(300)







