# 教育机构：马士兵教育
# 讲    师：杨淑娟

#函数的调用，通过函数名调用
def show():
    print('''helloworld''')

show() # 调用函数
import  openpyxl
filename='salary.xlsx'
#模拟银行发工资  def是定义函数的关键字
def getsalary(cardno,account,salary):
    # 在Python中格式化字符串有三种方式，%   ，format函数，简写的f
    print(f'账户名称为{account}的{cardno}实发工资{salary}元')

def getemp(filename):
    lst=[]
    wk=openpyxl.load_workbook(filename)
    sheet=wk.active # 获取当前活动的sheet页
    rows=sheet['A2:C4']
    for row in rows:
        sub_lst=[]
        for cell in row:
            sub_lst.append(cell.value)
        lst.append(sub_lst)
    return  lst

def start():
    lst=getemp(filename) #调用获取员工列表的函数
    for item in lst: #每一个item就是列表中一个员工的数据
        getsalary(item[0],item[1],item[2]) #调用获取薪水的函数


#以主函数的形式运行
if __name__ == '__main__':
    start()