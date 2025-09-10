# coding=utf-8
# 不归入梦，盏茶寄情
# 月念尘
import os
from pdf2docx import Converter
import time
from alive_progress import alive_bar
from PyPDF2 import PdfFileReader

"""file_path = os.getcwd()
# print(pdf_path)

files = os.listdir(file_path)
# 遍历所有文件
for file in files:

    # 过滤临时文件
    if '~$' in file:
        continue

    # 过滤非pdf格式文件
    if file.split('.')[-1] != 'pdf':
        continue
    # 获取文件名称
    file_name = file.split('.')[0]
    # print(file_name)
    # pdf文件名称
    pdf_path = file_name + '.' + file.split('.')[-1]"""


# 第三步：定义相对应的函数
def get_num_pages(pdf_path):
    """
    获取文件总页码
    :param pdf_path: 文件路径
    :return:
    """
    reader = PdfFileReader(pdf_path)
    # 不解密可能会报错：PyPDF2.utils.PdfReadError: File has not been decrypted
    if reader.isEncrypted:
        reader.decrypt('')
    page_num = reader.getNumPages()
    return page_num


def pdf_docx():
    """    # 获取当前工作目录
    file_path = os.getcwd()
    print(file_path)

    # 获取所有文件
    files = os.listdir(file_path)

    print(files)

    # # 遍历所有文件
    for file in files:

        # 过滤临时文件
        if '~$' in file:
            continue

        # 过滤非pdf格式文件
        if file.split('.')[-1] != 'pdf':
            continue
        # 获取文件名称
        file_name = file.split('.')[0]
        # print(file_name)
        # pdf文件名称
        pdf_name = os.getcwd() + '\\' + file
        # pdf_name = r'D:\python37Project_pdf_word\a.pdf'

        # pdf_name = f'{pdf_name}.pdf'
        # print(pdf_name)
        #     # docx文件名称
        docx_name = os.getcwd() + '\\' + file_name + '.docx'
        # docx_name = r'D:\python37Project_pdf_word\a.docx'

        # print(docx_name)
        # 加载pdf文档"""

    cv = Converter(pdf_path)
    docx_path = pdf_path.split('.')[0] + '.docx'
    # cv.parse()
    cv.convert(docx_path)
    cv.close()


if __name__ == '__main__':
    pdf_path = input('请输入pdf文件路径:')
    result = get_num_pages(pdf_path)
    with alive_bar(len(range(result)), force_tty=True) as bar:
        for item in range(result):
            bar()
            time.sleep(0.05)
    pdf_docx()
    os.system('pause')
