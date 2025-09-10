# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟
import glob
print('--------------递归遍历所有文件夹中的文件---------------')
print(glob.glob('**/*.py',recursive=True))
