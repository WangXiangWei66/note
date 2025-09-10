# coding:utf-8
# author:杨淑娟
import PyPDF2,glob   # PyPDF2  操作PDF文件的 第三方模块，需要安装才能使用 pip install PyPDF2
filenames=[]         # 用于存储指定路径下）所有的(pdf)文件名
# 获取指定路径下所有的pdf文件
for filename in glob.glob(r'file/*.pdf'):
    filenames.append(filename)
print(filenames)   # 测试，输出所有的文件路径 （filenames）每个元素都是包含路径

for i in filenames:   # 遍历所有的PDF文件
    pdffile = open(i,'rb')    # 以二进制读取模式打开PDF文件

    # 创建PDF文件的读取器，目的是从pdffile中读取PDF文件中的内容
    pdfreader = PyPDF2.PdfFileReader(pdffile)

    # 创建PDF文件的写入器，目的是将数据写进到PDF文件
    pdfwrite1 = PyPDF2.PdfFileWriter()

    # 获取当前的PDF的总页数
    all_page = pdfreader.numPages
   # PDF文件，页码的索引 ，如果文件是3页，那么页码的索引是0，1，2

    for page in range(0,all_page-1): # 为什么all_page-1？因为最后一页不写入（删除）
    #     #去除不想要的页面
          # 想要删除第二页和最后一页
          if page==1:   # 第二页码的索引是1 ，
              continue       # 后续的代码不执行，跳到循环处（ for page in range(0,all_page-1)
          pageobj = pdfreader.getPage(page)  # 读取当前这页的内容

          pdfwrite1.addPage(pageobj)  # 添加到PDF写入器的对象中
          # i[:len(i)-4]  去掉文件中的 .pdf
    f1 = open(i[:len(i)-4]+'-new.pdf','wb')  # 使用二进制写入的方式将数据写到PDF文件中
    pdfwrite1.write(f1) # 写入
    pdffile.close() # 关闭
    f1.close() # 关闭
