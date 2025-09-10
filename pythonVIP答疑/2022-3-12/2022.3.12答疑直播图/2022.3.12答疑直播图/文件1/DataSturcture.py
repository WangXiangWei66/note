class Node():
    def __init__(self,data):
        # 数据
        self.data=data
        # 节点
        self.pointer=None

# 单链表
class SingleLinkList():
    # 头结点指向节点
    def __init__(self,Node=None):
        self.head=Node

    def is_empty(self):
        if self.head==None:
            return True

    def get_length(self):
        count=0
        current=self.head
        if self.is_empty():
            print("空的单链表")
            return 0
        else:
            while current!=None:
                count+=1
                current=current.pointer
            return count

    def loop_list(self):
        len=self.get_length()
        if len!=0:
            i=0;
            current = self.head
            while i<len:
                print(current.data,end=", ")
                current=current.pointer
                i+=1
        print()

    def add_element(self,index,element):
        node=Node(element)
        # 头插法
        if index==0:
            node.pointer=self.head
            self.head=node
        else:
            # 尾插法
            if index==-1:
                current=self.head
                while current.pointer!=None:
                    current = current.pointer
                    current.pointer=None
                current.pointer=node
            else:
                current = self.head
                count=0
                while current.pointer!=None:
                    current = current.pointer
                    count+=1
                    if count==index:
                        # node=Node(element)
                        node.pointer=current.pointer
                        current.pointer=node
        print("元素插入成功！")

    def delete_element(self,element):
        current = self.head
        pre=None
        if current.data==element:
            self.head=current.pointer
        else:
            while current!= None:
                if element==current.data:
                    pre.pointer=current.pointer
                    current.pointer=None
                    print("元素删除成功！")
                    return
                else:
                    pre=current
                    current=current.pointer
            else:
                print("not found.......")

    def find_element(self,element):
        current=self.head
        while current!=None:
            if element==current.data:
                print("element found!!")
                return
            else:
                current=current.pointer
        else:
            print("element not found!!")

if __name__ == '__main__':
    n1=Node(100)
    lst=SingleLinkList(n1)
    lst.add_element(-1,200)
    lst.add_element(-1,400)
    lst.add_element(0,300)
    lst.add_element(2,800)
    lst.add_element(3,100)
    lst.loop_list()
    print("*"*6)
    print("lst.delete_element(400)" )
    lst.delete_element(400)
    lst.loop_list()
    print("lst.delete_element(500)" )
    lst.delete_element(500)
    lst.loop_list()
    lst.delete_element(300)
    print("lst.delete_element(100)")
    lst.delete_element(100)
    lst.loop_list()
    print("lst.find_element(200)")
    lst.find_element(200)
    print("*" * 6)
    print("lst.find_element(300)")
    lst.find_element(300)







