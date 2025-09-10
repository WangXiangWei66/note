class Stack:
    def __init__(self):
        self.st=[]

    def get_length(self):
        return len(self.st)

    # FILO
    def add_data(self,element):
            self.st.append(element)

    def remove_data(self,element):
        count=self.get_length()
        for i in range(count,0,-1):
            value=self.pop_data(i-1)
            if element==value:
                self.st.remove(element)
                print(f"deleted element {element}!!")
                # return
        else:
            print(f"not found element {element}...........")

    def look_for(self):
        if len(self.st)==0:
            print("empty stack.........")
        else:
            for i in self.st:
                print(i,end="  ")
        print()

    def pop_data(self,cap):
        if len(self.st)==0:
            print("empty stack.........")
        else:
            return self.st[cap]

if __name__ == '__main__':
    s=Stack()
    s.add_data(2)
    s.add_data("hello")
    s.add_data(3.65)
    s.add_data(2)
    s.add_data(7.3)
    print(s.get_length())
    s.look_for()
    s.remove_data(5)
    s.remove_data(2)
    print(s.get_length())
