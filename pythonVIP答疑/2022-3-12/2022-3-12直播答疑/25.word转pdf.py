# coding:utf-8
# author:杨淑娟

from win32com.client import constants, gencache
import os.path

def createPdf(wordPath, pdfPath):

	word = gencache.EnsureDispatch('Word.Application')  #打开Word这个应用程序
	doc = word.Documents.Open(wordPath, ReadOnly=1)
	doc.ExportAsFixedFormat(pdfPath,
	                        constants.wdExportFormatPDF,  # 将word导出 PDF
	                        Item=constants.wdExportDocumentWithMarkup,
	                        CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
	word.Quit(constants.wdDoNotSaveChanges)


if __name__ == '__main__':  # 右键 运行时，if之下的代码才会执行，如果该 文件（模块）被导入到其它模块中，if中的代码不执行
	# word 文件所在路径
   path=r'D:\pythonpro\2022-3-12直播答疑\file'
   #获取这个路径下的所有文件
   lst=os.listdir(path)

   for item in lst:
       if item.endswith('.docx'): # 判断是否是world文件
			# 调用转换的函数，进行将word转成PDF
			 #  第一个参数是 待转换的word文件
			# 第二个参，  转换后pdf文件的路径和名称    item.split('.')[0]获取word文件的文件名
            createPdf(path+'//'+item, path+'//'+item.split('.')[0]+'.pdf')