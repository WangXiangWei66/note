# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
# 办公自动化方向--》使用Python去操作Excel文件
'''
从一个大的Excel文件中提取符合条件的数据，单独存储到一个独立的Excel文件中
将Excel文件中的内容读取到Python程序中有以下几种方式
  a)使用xlrd  模块
  b)使用openpyxl模块
  c)使用pandas模块   --》数据分析中的模块
  以上三个模块都是第三方模块，都需要进行安装   pip install  模块名称 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com


'''
import  pandas as pd
data_frame=pd.read_excel('一网通.xlsx')  #data_frame相当于一个二维表，有行有列
lst=data_frame.values
new_lst=[]  #新的列表，相当于表
for item in lst:   #item 表示的是每一行数据
    for data in item:  #data表示的是每一列数据
        if data=='一网通业务帐户':
            new_lst.append(item)  #item相当于表中的行

df=pd.DataFrame(new_lst,columns=['部门','集团名称','客户经理','无用','集团编号','账户名称','集团账户标识','付费方式','欠费','充值金额','始欠月',
                                 '19年是否处理过','19年坏账确认','一年以上欠费差额'])
df.to_excel('一网通业务账户.xlsx',index=False)





