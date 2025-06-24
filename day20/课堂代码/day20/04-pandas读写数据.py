"""
pandas读写数据：
  1. 在pandas中读数据的方法： read_xxx
  2. 在pandas中写数据的方法： to_xxx

read_csv()
        csv： comma seperator value  逗号分隔值

read_table(): 按照制表符分隔的数据
read_excel()

"""
import pandas as pd

# df01 = pd.read_csv("a.csv", index_col="id")
# 如果加载的文件系统中的文件， 需要安装fsspec
df01 = pd.read_csv("D://b.csv", header=None)
print(df01)

print("---------------------------------")
# 读取excel， 需要安装openpyxl
df02 = pd.read_excel("D://info.xlsx", index_col="uid")
print(df02)

print("---------------------------------")
# sep 指定数据的分隔符
df03 = pd.read_table("a.csv", sep=",")
print(df03)
