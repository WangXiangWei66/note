# 工作室名称：Mall Data
# 攻 城 狮：穿越~
import os
filename='student.txt'
def main():
    while True:
        menum()
        choice=int(input('请输入您选择的序号：（如2）'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定退出系统吗？ y/n ')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
        else:
            print('您的输入有误，请输入0~7序号。谢谢!')
def menum():
    print('===============学生信息管理系统=======================')
    print('---------------功能菜单--------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排名学生成绩')
    print('\t\t\t\t\t\t6.统计学生总数')
    print('\t\t\t\t\t\t7.显示全部学生信息')
    print('\t\t\t\t\t\t0.退出本系统')
    print('-----------------------------------------------')
def insert():#1录入学生信息
    stu_list=[]
    while True:
        id=input('请输入学生ID号（如，1001）：')
        if not id:
            break
        #加入判断ID不重复的代码，遍历字典中ID。如果重复，则提示，id已经存在，请确认ID信息。
        result= find_id(id)
        if result:
            print('学号重复，请重新输入')
            continue

        name=input('请输入学生名字：')
        if not name:
            break
        try:
            englist=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            java=int(input('请输入java成绩：'))
            C=int(input('请输入C语言成绩：'))
        except:
            print('输入无效，请输入0~100的整数，请重新输入')
            continue
        #将录入的学生信息保存到字典
        student={'id':id,'name':name,'enflist':englist,'python':python,'java':java,'C':C}
        stu_list.append(student)
        answer=input('是否继续添加？y或n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #调用save()函数
    save(stu_list)
    print('学生信息录入成功，并保存！')
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()







def search():#2查找学生信息
    pass
def delete():#3删除学生信息
    while True:
        student_id=input('请输入要删除的学生ID：')
        if not student_id:
            if os.path.exists(filename):#判断文件是否存在，如果存在。
                with open(filename,'r',encoding='utf-8') as rfile:#以只读的方式，打开文件。并放在文件名为file的中
                    student_old=rfile.readlines()#读取所有文件
            else:#如果，没有文件
                student_old=[]#建立一个空列表
            flag=False  #标记是否已经删除
            if student_old:#如果列表有值（内容）
                with open(filename,'w',encoding='utf-8') as wfile:#以只写的方式打开文件，并命名为wfile。
                    d={} #定义一个空字典，将未删除的学生信息覆盖到原文件
                    for i in student_old:
                        d=dict(eval(i))#将遍历的字符串转成字典
                        if d['id']!=student_id:#如果字典中的ID与要删除的ID不同则
                            wfile.write(str(d)+'\n') #将字典内容转换为字符串，写入文件中，并\n换行。
                        else:
                            flag=True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息，请确认ID输入是否正确')
            else:
                print('无学生信息')
                break
            show() #删除之后要重新显示所有学生信息
            ans=input('是否继续删除？y或n\n')
            if ans=='y' or ans=='Y':
                continue
            else:
                break

def modify():#4修改学生信息

        show()
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as rfile:
                student_old=rfile.readlines()
        else:
            return
        student_id=input('请输入某位学生的ID：')
        #加判断输入是否为空
        with open(filename,'w',encoding='utf-8') as wfile:
            for item in student_old:
                d=dict(eval(item))
                if d['id']==student_id:
                    print(f'找到了ID为{student_id}的学生，可以修改该学生的相关信息了！')
                    while True:
                        try:
                            d['name']=input('请输入新名字：')
                            d['enflist'] = input('请输入英语新成绩：')
                            d['python'] = input('请输入python新成绩：')
                            d['java'] = input('请输入java新成绩：')
                            d['C'] = input('请输入C语言新成绩：')
                            break
                        except:
                            print('您输入的信息有误，请重新输入！！！')
                        # else:
                        #     break
                    wfile.write(str(d)+'\n')
                    print('修改成功！！！')

            else:
               wfile.write(str(d) + '\n')
        answer=input('是否继续修改其他学生信息？ y/n :')
        if answer=='y' or answer=='Y':
            modify()

def sort():#5成绩排序
    pass
def total():#6统计学生信息
    pass
def show():#7显示所有学生信息
    pass


def find_id(id):
    # 读取学生信息
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()

    with open(filename, 'w', encoding='utf-8') as wfile:

        for item in student_old:
            d = dict(eval(item))
            if id==d['id']:
                return True
    return False

if __name__ == '__main__':
    main()




