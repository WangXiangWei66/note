#liuyifei
#开发时间:2022/3/31 13:51
import os
import pdfplumber
import re

cont=J = M = C = D = N = S = P = I = R = 0
# 创建三个列表
lst_papers=[]
lst=[]
size=[]
# 想要提取内容的文件的路径
path='./file'

datanames=os.listdir(path) # 获取当前路径下的所有文件名 ，结果是一个列表类型

print('指定路径下的所有文件名',datanames) # 结果

# 从所有文件名中提取pdf文件
for item in datanames:
    if item.endswith('.pdf'):
                        # 拼接完整路径
        lst_papers.append('file/'+item)  # 将提取的pdf文件存储到列表中

#lst_papers 存储的是所有pdf文件的路径

print(lst_papers) # 构建完整理路径存放到列表lst_papers中

for item in lst_papers:   # 遍历pdf文件所有的列表（列表中是文件的完整路径）
    with pdfplumber.open(item)as pdf:     # 使用第三方模块pdfpumber读取pdf文件
        for index in range(len(pdf.pages)):  #  获取当前pdf文页的索引（如果文件有10页，页码索引为0到9
            pdf_page=pdf.pages[index] # 获取当前pdf页  ,如果index为0则获取到的是第一页pdf文件
            # 提取pdf文件中的内容，将 '「'使用'['替代，将'」'使用']'去替代
            content=pdf_page.extract_text().replace('「','[').replace('」',']') # 提取内容并替换
             # content为pdf页面中的内容，结果是str类型
            #print(content)
            J += content.count('［J］')#所有文章J 引文的总数

            M+=content.count('[M]')#每篇文字M引文的数量
            C+=content.count('[C]')
            N+= content.count('[N]')
            D+= content.count('[D]')
            R += content.count('[R]')
            S += content.count('[S]')
            P += content.count('[P]')
            I += content.count('[I]')
            total=J+M+C+N+D+R+S+P+I
        #print(J,'-----------------------')

print(total) #