# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

# calorie=100*28
# print(f'今天{calorie},{calorie/1000}')
class Student():
    def __init__(self,name,age,java,html,sql):
        self.name=name
        self.age=age
        self.java=java
        self.html=html
        self.sql=sql
    def info(self):
        print(self.name,self.age,self.java,self.html,self.sql)
#
class SystemStudent():
    def __init__(self):
         self.lst=[]
    def insert(self,stu):
        self.lst.append(stu)
    def query(self):
        for item in self.lst: #item实际上它是学生对象
            item.info() #对象名.方法名（）

if __name__ == '__main__':
    stu1=Student('张三',20,90,80,100)
    stu2 = Student('张三2', 20, 90, 80, 100)
    stu3 = Student('张三3', 20, 90, 80, 100)
    sysstu=SystemStudent()
    sysstu.insert(stu1) # 新增学生
    sysstu.insert(stu2)  # 新增学生
    sysstu.insert(stu3)  # 新增学生
    sysstu.query()
