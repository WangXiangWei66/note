#教育机构 ：马士兵教育
#讲    师：杨淑娟
#开发时间：2020/4/12 18:38
#主函数
import os
import time
filename='students.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择:'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您确定要退出系统吗?y/n')
                if answer=='y'or answer=='Y':
                    print('谢谢您的使用!!!')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert() #录入学生信息
            elif choice==2:
                search() #查询学生信息
            elif choice==3:
                delete() #删除学生成绩信息
            elif choice==4:
                modify() #修改学生成绩信息
            elif choice==5:
                sort() #排序
            elif choice==6:
                total() #统计学生总数
            elif choice==7:
                show()


def menu():
    #输出菜单
    print('''===================学生信息管理系统========================
------------------------功能菜单---------------------------
             1.录入学生信息
             2.查找学生信息
             3.删除学生信息
             4.修改学生信息
             5.排序
             6.统计学生总人数
             7.显示所有学生信息
             0.退出系统
----------------------------------------------------------
    ''')
def insert():
    student_list=[]
    while True:
        id=input('请输入ID(如1001):')
        if not id:                       #id为空，跳出循环
            break
        name=input('请输入姓名:')
        if not name:                    #name为空，跳出循环
            break
        try:
            english=int(input('请输入英语成绩:'))
            python=int(input('请输入Python成绩:'))
            java=int(input('请输入Java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入!!!')
            continue

        #将录入的学生信息保存到字典
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
           #将学生字典添加到列表中
        student_list.append(student)
        answer=input('是否继续添加?y/n\n')
        if answer=='y':                  #继续添加
            continue
        else:                            #不继续添加
            break
    save(student_list)                   #将学生信息保存到文件
    print('学生信息录入完毕!!!')


def search():
    student_query=[]                    #保存查询结果的学生列表
    while True:
        id=''
        name=''
        if os.path.exists(filename):                          #判断文件是否存在
            mode=input('按ID查找请输入1，按姓名查询请输入2:')
            if mode=='1':
                id=input('请输入学生ID:')
            elif mode=='2':
                name=input('请输入学生姓名:')
            else:
                print('您的输入有误，请重新输入!!!')
                search()                                         #重新查询
            with open(filename,'r',encoding='utf-8') as rfile:   #打开文件
                student=rfile.readlines()                        #读取文件中全部内容
                for item in student:
                    d=dict(eval(item))                           #字符串转字典
                    if id!='':                                   #判断是否按ID查询
                        if d['id']==id:
                            student_query.append(d)              #将找到的学生信息保存到列表中
                    elif name!='':
                        if d['name']==name:                   #判断是否按姓名查询
                            student_query.append(d)              #将找到的学生信息保存到列表中
            show_student(student_query)                      #显示查询结果
            student_query.clear()                            #清空列表
            answer=input('是否继续查询?y/n\n')
            if answer=='y':
                 continue
            else:
                 break
        else:
            print('暂未保存学生信息!!!')
            return
def delete():
    while True:
        student_id=input('请输入要删除的学生的ID:')
        if student_id !='':                  #判断要是否录入要删除的学生
            if os.path.exists(filename):          #判断文件是否存在
                with open(filename,'r',encoding='utf-8') as file:  #打开文件
                    student_old=file.readlines()  #读取全部内容
            else:
                student_old=[]
            flag=False                            #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile: #以写方式打开文件
                    d={}                          #定义空字典
                    for item in student_old:
                        d=dict(eval(item))        #字符串转字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n') #将一条学生信息写入文件
                        else:
                            flag=True                #标记已删除
                    if flag:
                        print('id为{}的学生信息已被删除!!!'.format(student_id))
                    else:
                        print('没有找到id为{}的学生信息。'.format(student_id))
            else:
                print('无学生信息!!!')
                break                               #退出循环
            show()                                  #显示全部学生信息
            answer=input('是否继续删除?y/n\n')
            if answer=='y':
                continue                            #继续删除
            else:
                break                               #退出删除学生信息功能'

def modify():
    show()                                                 #显示全部学生信息
    if os.path.exists(filename):                           #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile: # 打开文件
            student_old=rfile.readlines()                  #读取全部内容
    else:
        return
    student_id=input('请输入要修改的学员ID:')
    with open(filename,'w',encoding='utf-8') as wfile:    #以只写模式打开文件
        for item in student_old:
            d=dict(eval(item))                            #字符串转字典
            if d['id']==student_id:                       #是否为要修改的学生
                print('找到这名学生，可以修改他的相关信息了!')
                while True:
                    try:
                        d['name']=input("请输入姓名:")
                        d['english']=input('请输入英语成绩:')
                        d['python']=input('请输入Python成绩:')
                        d['java']=input('请输入Java成绩:')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break                             #退出循环
                wfile.write(str(d)+'\n')                  #将修改的信息写入文件
                print('修改成功!!!')
            else:
                wfile.write(str(d)+'\n')                  #将未修改的信息写入文件

    answer=input('是否继续修改其他学生信息?y/n\n')
    if answer=='y':
            modify()                                  #重新执行修改操作


def sort():
    show()                                                        #显示全部学生信息
    if os.path.exists(filename):                                  #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:        #打开文件
            student_list=rfile.readlines()                        #读取全部学生信息
        student_new=[]
        for item in student_list:
            d=dict(eval(item))                                    #将字符串转字典
            student_new.append(d)                              #将转换后的字典添加到列表中
    else:
        return
    asc_or_desc=input('请选择(0升序,1降序):')
    if asc_or_desc=='0':                                         #按升序排序
        asc_or_desc_bool=False
    elif asc_or_desc=='1':                                       #按降序排序
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入!')
        sort()
    mode=input('请选择排序方式(1.按英语成绩排序,2.按Python成绩排序,3.按Java语言成绩排序，0.按总成绩排序):')
    if mode=='1':                                               #按英语成绩排序
        student_new.sort(key=lambda x: int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':                                             #按python成绩排序
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode=='3':                                              #按java成绩排序
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda x:int(x['english'])+int(x['python'])+int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入!!!')
        sort()
    show_student(student_new)                                  #显示排序结果
def total():
    if os.path.exists(filename):                          #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as rfile:#打开文件
            students=rfile.readlines()                    #读取全部内容
            if students:
                print('一共有{}名学生。'.format(len(students)))
            else:
                print('还没有录入学生信息。')
    else:
        print('暂未保存数据信息...')
def show():
    student_list=[]
    if os.path.exists(filename):                                 #判断文件是否存在
        with open(filename,'r',encoding='utf-8')as rfile:        #打开文件
            students=rfile.readlines()                           #读取全部数据
        for item in students:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)                           #调用显示学生信息的方法
    else:
        print('暂未保存数据信息!!!!')

def show_student(query_student):
    if len(query_student)==0:
        print('没有查询到学生，无数据可显示!!!')
        return
    #定义标题显示格式
    format_tile='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_tile.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容显示格式
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in query_student:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))

#用于保存学生信息到磁盘文件
def save(students):
    try:
        student_txt=open(filename,'a',encoding='utf-8')    #以追加模式打开
    except Exception as e:
        student_txt = open(filename, 'w',encoding='utf-8') #文件不存在， 创建并打开
    for item in students:
        student_txt.write(str(item)+'\n')       #按行存储，添加换行符
    student_txt.close()                         #关闭文件


if __name__ == '__main__':
    main()