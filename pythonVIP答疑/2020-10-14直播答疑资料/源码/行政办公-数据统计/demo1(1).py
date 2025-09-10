#教育机构 ：马士兵教育
#讲    师：杨淑娟
#(1)导入使用到的模块
import  xlrd   #用于从Excel中读取数据
import  xlsxwriter   #用于向Excel文件中写数据
import  os    #使用os中的方法，获取指定目录下的所有文件

'''(2)使用Python去新建一个Excel文件'''
workbook=xlsxwriter.Workbook('马士兵教育疫情期间员工离京情况统计汇总.xlsx')  #workbook对应磁盘上一个名称为xxx的Excel文件

'''(3)创建一个工作表 ，所说的sheet表 '''
worksheet=workbook.add_worksheet()

'''设置单元格的样式(标题)'''
bold_center=workbook.add_format({'align':'center','valign':'vcenter','font_size':18,'border':1})
'''设置细节标题的样式'''
bold=workbook.add_format({'bold':True,'align':'center','valign':'vcenter','border':1,'bg_color':'#dddddd','color':'#000000'})
bold1=workbook.add_format({'bold':True,'align':'center','valign':'vcenter','border':1,'bg_color':'#ffffff','color':'#000000'})
bold_cell=workbook.add_format({'align':'center','valign':'vcenter','border':1})
'''合并单元格'''
worksheet.merge_range('A1:H2','公司名称:马士兵(北京)教育科技有限公司',bold_center)

worksheet.merge_range('A3:A4','序号',bold)
worksheet.merge_range('B3:B4','姓名',bold1)
worksheet.merge_range('C3:C4','是否离京',bold)
worksheet.merge_range('D3:D4','进京时间',bold)
worksheet.merge_range('E3:F3','从何处进京',bold)
worksheet.write('E4','省',bold)
worksheet.write('F4','市',bold)
worksheet.merge_range('G3:G4','上班时间',bold)
worksheet.merge_range('H3:H4','备注',bold)
'''获取指定目录下的所有文件'''
files=os.listdir('data/')
num=1   #人员的序号
n=5     #单元格的序号
for item in files:
    if  item.endswith('.xlsx'):   #过滤掉非Excel文件
        #打开Excel文件
        file=xlrd.open_workbook('data/'+item)  #open_workbook(path)
        #使用指定的sheet页
        info=file.sheet_by_index(0)   #0代表的是第一个sheet页
        #获取指定的单元格的值
        name=info.cell(4,1).value   #行和列的索引从0开始
        leave_beijing=info.cell(4,2).value
        in_beijing_time=info.cell(4,3).value
        province=info.cell(4,4).value
        city=info.cell(4,5).value
        work_time=info.cell(4,6).value
        remark=info.cell(4,7).value
        #print(name,leave_beijing,in_beijing_time,province,city,work_time,remark)
        '''把获取到的数据写到新的Excel文件中'''
        #worksheet.write('A{}'.format(n),num,bold_cell)  #在  A5,A6,A7,A8....
        worksheet.write('A'+str(n),num,bold_cell)
        worksheet.write('B{}'.format(n),name,bold_cell)
        worksheet.write('C{}'.format(n),leave_beijing,bold_cell)
        worksheet.write('D{}'.format(n),in_beijing_time,bold_cell)
        worksheet.write('E{}'.format(n),province,bold_cell)
        worksheet.write('F{}'.format(n),city,bold_cell)
        worksheet.write('G{}'.format(n),work_time,bold_cell)
        worksheet.write('H{}'.format(n),remark,bold_cell)
        print('完成'+item+'数据提取')  #完成了哪个文件的数据提取
        num+=1    #写完一行数据之后，人员序号加1
        n+=1      #单元格的行号+1


workbook.close()





















