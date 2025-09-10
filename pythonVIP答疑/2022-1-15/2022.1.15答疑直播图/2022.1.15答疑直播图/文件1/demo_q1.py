#开发时间：2022/1/11 10:03

def main():
    while True:
        menm()
        try:
            choice = int(input('请选择'))
        except ValueError:
            choice = -1

        switcher={0:quit,1:insert,2:search,3:delete,4:modify,5:sort,6:total,
                  7:show}
        switcher[-1]=others
        switcher.get(choice,others)()
'''
        if choice in list(range(8)):
            if choice==0:
                answer = input('你确定要退出吗？y/n')
                if answer == 'y' or answer == 'n':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert() #录入学生信息
            elif choice==2:
                search('hi') #
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
'''
def menm():
    print('=========================学生信息管理系统===========================')
    print('------------------------------功能菜单------------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('----------------------------------------------------------------')

def quit():
    answer = input('你确定要退出吗？y/n')
    if answer == 'y' or answer == 'n':
        print('谢谢您的使用！！！')
        # break
        exit()
    else:
        # continue
        return
def others():
    pass

def insert():
    # pass
    print('hello')
def search(str1):
    # pass
    print(str1)
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


if __name__=='__main__':
    main()
    print('88，感谢使用！')
