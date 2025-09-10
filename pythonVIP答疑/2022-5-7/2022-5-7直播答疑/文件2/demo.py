#liuyifei
#开发时间:2022/3/31 13:51
import os
import pdfplumber
import re
import openpyxl
from openpyxl.styles import Font,Alignment
from openpyxl.chart import BarChart,Reference
cont=J = M = C = D = N = S = P = I = R = 0
# file_name=os.listdir() # 获取当前文件路径
# print(file_name)
lst_papers=[]
lst=[]
size=[]
path='file'
datanames=os.listdir(path)
print(datanames)
year=datanames[0].split('(')[0]
lst.append(year)

for item in datanames:
    if item.endswith('.pdf'):
        lst_papers.append('file/'+item)
lst.append(len(lst_papers))
for item in lst_papers:
    with pdfplumber.open(item)as pdf:
        for index in range(len(pdf.pages)):
            pdf_page=pdf.pages[index]
            content=pdf_page.extract_text().replace('「','[').replace('」',']')

            print(re.compile('\[\d+\]').findall(content,re.MULTILINE))
            J += content.count('[J]')#所有文章J 引文的总数
            M+=content.count('[M]')#每篇文字M引文的数量
            C+=content.count('[C]')
            N+= content.count('[N]')
            D+= content.count('[D]')
            R += content.count('[R]')
            S += content.count('[S]')
            P += content.count('[P]')
            I += content.count('[I]')
            cont += content.count('[I]') + content.count('[C]') + content.count('[P]') + content.count('[R]') + content.count('[S]') + content.count('[N]') + content.count('[D]') + content.count('[M]') + content.count('[J]')
            total=J+M+C+N+D+R+S+P+I

        print(cont)