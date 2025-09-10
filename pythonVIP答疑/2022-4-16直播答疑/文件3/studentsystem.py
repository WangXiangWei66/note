#!user/bin/python
# -*- coding: utf-8 -*-
# 开发时间：2022/4/13 0013 14:57
import os.path

filename = 'student.txt'


def main():
    while True:
        menu()
        try:
            answer = int(input('请输入:'))
        except:
            print('输入有误，请重新输入！')
        else:
            if answer in [0, 1, 2, 3, 4, 5, 6, 7]:
                if answer == 0:
                    choice = input('您确定要退出系统吗？y/n')
                    if choice == 'y' or choice == 'Y':
                        break
                    else:
                        continue
                elif answer == 1:
                    insert()
                elif answer == 2:
                    delete()
                elif answer == 3:
                    modify()
                elif answer == 4:
                    search()
                elif answer == 5:
                    sort()
                elif answer == 6:
                    total()
                elif answer == 7:
                    show()
                else:
                    print('输入有误，请重新输入')
                    continue


def menu():
    print('=======================学生信息管理系统==============================================')
    print('--------------------------功能菜单-------------------------------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.删除学生信息')
    print('\t\t\t\t\t3.修改学生信息')
    print('\t\t\t\t\t4.查询学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出系统')
    print('---------------------------------------------------------------------------------')


def insert():
    student_lst = []
    while True:
        student_name = input('请输入要录入学生的姓名：')
        if student_name != '':
            try:
                student_id = int(input('请输入要录入学生id：'))
            except:
                print('输入有误,请重新输入')
                continue
            else:
                try:
                    english = int(input('请输入英语成绩：'))
                    python = int(input('请输入python成绩：'))
                    java = int(input('请输入java成绩：'))
                except:
                    print('输入有误，请重新输入！')
                    continue
                else:
                    d = {'id': student_id, 'name': student_name, 'english': english, 'python': python, 'java': java}
                   # d = {'id': student_id, '姓名': student_name, 'english': english, 'python': python, 'java': java}
                    student_lst.append(d)
                    answer = input('是否继续录入信息？y/n')
                    if answer == 'y' or answer == 'Y':
                        continue
                    else:
                        save(student_lst)
                        print('学生信息已录入完毕！')
                        break
        else:
            print('输入有误，请重新输入')
            continue


def save(lst):
    if lst:
        for item in lst:
            try:
                with open(filename, 'a', encoding='utf-8') as afile:
                    afile.write(str(item) + '\n')
            except:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    wfile.write(str(item) + '\n')
    else:
        print('未存入学生信息')
        return


def delete():
    student_new = []
    while True:
        del_id = input('请输入要删除学生的id：')
        if del_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as rfile:
                    student = rfile.readlines()
                flag = False
                if student:
                    for item in student:
                        d = dict(eval(item))
                        if d['id'] != int(del_id):
                            student_new.append(d)
                        else:
                            flag = True
                    with open(filename, 'w', encoding='utf-8') as wfile:
                        for item in student_new:
                            wfile.write(str(item) + '\n')
                    if flag:
                        print('该学生信息已被删除！')
                    show()
                    answer = input('是否继续删除学生？y/n')
                    if answer == 'y' or answer == 'Y':
                        delete()
                    else:
                        return
                else:
                    print('暂未录入学生信息')
                    return
            else:
                print('本地学生数据信息不存在！')
                return


def modify():
    student_old = []
    while True:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
            mo_id = input('请输入要修改的学生id：')
            if student:
                for item in student:
                    d = dict(eval(item))
                    if d['id'] == int(mo_id):
                        while True:
                            try:
                                new_id = int(input('请输入修改后的id：'))
                                new_name = input('请输入修改后的姓名：')
                                new_english = int(input('请输入修改后的英语成绩：'))
                                new_python = int(input('请输入修改后的python成绩：'))
                                new_java = int(input('请输入修改后的java成绩：'))
                            except:
                                print('输入有误，请重新输入')
                                continue
                            else:
                                d = {'id': new_id, 'name': new_name, 'english': new_english, 'python': new_python,
                                     'java': new_java}
                                student_old.append(d)
                                break
                    else:
                        student_old.append(d)
                with open(filename, 'w', encoding='utf-8') as wfile:
                    for item in student_old:
                        wfile.write(str(item) + '\n')
                    answer = input('是否继续修改学生信息？y/n')
                    if answer == 'y' or answer == 'Y':
                        continue
                    else:
                        return
            else:
                print('该学生信息不存在')
                choice = input('是否录入该学生信息?y/n')
                if choice == 'y' or choice == 'Y':
                    insert()
                else:
                    return
        else:
            return


def search():
    student_new = []
    student_name = []
    student_id = []
    while True:
        try:
            mode = int(input('请输入查询方式（1.查id 2.查姓名）'))
        except:
            print('输入有误，请重新输入！')
            continue
        else:
            if mode == 1:
                s_id = input('请输入要查询学生的id：')
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as rfile:
                        student = rfile.readlines()
                    if student:
                        for item in student:
                            d = dict(eval(item))
                            student_id.append(d['id'])
                        if int(s_id) in student_id:
                            for item in student:
                                d = dict(eval(item))
                                if d['id'] == int(s_id):
                                    student_new.append(d)
                                    show_student(student_new)
                                    break
                        else:
                            print('查询学生不在')
                        answer = input('是否继续查询？y/n')
                        if answer == 'y' or answer == 'Y':
                            search()
                        else:
                            return
                    else:
                        print('暂未存入学生信息')
                else:
                    print('学生信息文件不存在')
                    return
            elif mode == 2:
                s_name = input('请输入要查询学生的姓名：')
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as rfile:
                        student = rfile.readlines()
                    if student:
                        for item in student:
                            d = dict(eval(item))
                            student_name.append(d['name'])
                        if s_name in student_name:
                            for item in student:
                                d = dict(eval(item))
                                if d['name'] == s_name:
                                    student_new.append(d)
                                    show_student(student_new)
                                    break
                        else:
                            print('查询的学生不在系统内')
                        answer = input('是否继续查询？y/n')
                        if answer == 'y' or answer == 'Y':
                            search()
                        else:
                            return
                    else:
                        print('暂未存入学生信息')
                else:
                    print('学生信息文件不存在')
                    return
            else:
                print('输入有误，请重新输入')
                continue


def show_student(lst):
    if len(lst) == 0:
        return
    else:
        format_title = '  {:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        format_date = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('id', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
        for item in lst:
            print(format_date.format(item['id'], item['name'], item['english'], item['python'], item['java'],
                                     int(item['english']) + int(item['python']) + int(item['java'])))


def sort():
    student_date = []
    while True:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                if student:
                    for item in student:
                        d = dict(eval(item))
                        student_date.append(d)
                else:
                    print('暂未存入学生信息')
                    return
                mode = input('请输入排序方式（0.升序 1.降序）')
                if mode == '0':
                    flag = False
                elif mode == '1':
                    flag = True
                else:
                    print('输入有误，请重新输入')
                    sort()
                try:
                    method = int(input('请输入排序方式（1.按英语成绩排序 2.按python成绩排序 3.按java成绩排序 0.按总成绩排序）'))
                except:
                    print('输入有误，请重新输入')
                    continue
                else:
                    if method == 1:
                        student_date.sort(key=lambda x: x['english'], reverse=flag)
                        show_student(student_date)
                        return
                    elif method == 2:
                        student_date.sort(key=lambda x: x['python'], reverse=flag)
                        show_student(student_date)
                        return
                    elif method == 3:
                        student_date.sort(key=lambda x: x['java'], reverse=flag)
                        show_student(student_date)
                        return
                    elif method == 0:
                        student_date.sort(key=lambda x: int(x['english'] + int(x['python']) + int(x['java'])))
                        show_student(student_date)
                        return
                    else:
                        print('输入有误，请重新输入')
                        continue
        else:
            print('暂未存入学生信息')
            return


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print('系统内共有{}名学生'.format(len(student)))
            else:
                print('暂未存入学生信息')
    else:
        print('没有学生信息文件')
        return


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                for item in student:
                    d = dict(eval(item))
                    student_lst.append(d)
                show_student(student_lst)
            else:
                print('暂未存入学生信息')
                return
    else:
        print('暂未存入学生信息')
        return


if __name__ == '__main__':
    main()
