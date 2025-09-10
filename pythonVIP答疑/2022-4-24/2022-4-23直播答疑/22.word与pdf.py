# coding:utf-8
# author:杨淑娟
from win32com.client import  gencache
from win32com.client import constants
def createPdf(wordPath, pdfPath):
    # print(wordPath, pdfPath)
   word = gencache.EnsureDispatch('Word.Application')  #打开Word这个应用程序
   doc = word.Documents.Open(wordPath, ReadOnly=1)
   doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,  # 将word导出 PDF
                           Item=constants.wdExportDocumentWithMarkup,
                           CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
   word.Quit(constants.wdDoNotSaveChanges)

# 注意，word的路径和pdf的路径一定要绝对路径
if __name__ == '__main__':
    createPdf('d:/pythonpro/2022-4-23直播答疑/2022.4.23答疑直播问题.docx','d:/pythonpro/2022-4-23直播答疑/1.pdf')

