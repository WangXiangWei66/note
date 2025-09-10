# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

filename='student.txt'
def main():
    while True:
        menum()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用!!!')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert() #录入学生信息
            elif choice==2:
                search() #查找
            elif choice==3:
                delete() #删除
            elif choice==4:
                modify() #修改
            elif choice==5:
                sort() #排序
            elif choice==6:
                total() #统计
            elif choice==7:
                show() #显示
def menum():
    print('====================学生信息管理系统=====================')
    print('-----------------------功能菜单------------------------')
    print('\t\t\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t\t\t0.退出系统')
    print('==================================================================')
def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if id in student_list: #
               print('id重复，请重新输入') #
               continue
        if not id:
            break
        name=input('请输入姓名:')
        if not name:
            break
        try:
                english=int(input('请输入英语成绩:'))
                python=int(input('请输入python成绩:'))
                chinese=int(input('请输入语文成绩:'))
        except:
                print('输入无效，不是整数类型，请重新输入')
                continue #将录入的学生信息保存到字典中
        student={'id':id,'name':name,'英语':english,'python':python,'语文':chinese} #将学生信息添加到列表中
        student_list.append(student)
        answer=input('是否继续添加？y/n\n')
        if answer=='y':
                continue
        else:
                break #调用save()函数
        save(student_list)
        print('学生信息录入完毕!!!')
def save(lst):
            try:
                stu_txt=open(filename,'a+',encoding='utf-8')
            except:
                stu_txt=open(filename,'w',encoding='utf-8')
                for item in lst:
                    stu_txt.write(str(item)+'\n')
                stu_txt.close()
def search():
            pass
def delete():
            pass
def modify():
            pass
def sort():
            pass
def total():
            pass
def show():
            pass
if __name__ == '__main__':
            main()
