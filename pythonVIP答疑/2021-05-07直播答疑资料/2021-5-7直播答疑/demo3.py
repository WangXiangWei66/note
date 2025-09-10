# 教育机构：马士兵教育
# 讲    师：杨淑娟

# 遍历一个Excel文件的所有工作表
import  pandas as pd
df=pd.read_excel('a.xlsx',sheet_name=None) #sheet_name=None表示读取的是所有工作表
# 先输出所有工作表的名称
print(len(df.keys()))  # 输出工作的个数
for item in df.keys(): # df.keys()工作表名称的列表
    print(df[item])