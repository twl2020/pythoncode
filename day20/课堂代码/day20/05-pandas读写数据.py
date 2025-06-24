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

df01 = pd.read_csv("a.csv")
df02 = pd.read_csv("D://b.csv")
print(df01)

# 将df01的数据写入excel
# 在excel中写入单张表数据
# df01.to_excel("D://xxx.xlsx")

# 在excel中写入多张表数据， 需要使用ExcelWriter对象
with pd.ExcelWriter("D://yyyy.xlsx") as w:
    df01.to_excel(w, sheet_name="s1")
    df02.to_excel(w, sheet_name="s2")




