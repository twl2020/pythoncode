"""
1. 将以上的数据存入一个名为df的DataFrame对象中
2. 显示前5行数据
3. 查看第1、3、5行中第2、4、6列的数据
4. 显示李四销售化妆品的情况
5. 统计张三的上班次数
6. 将表头由中文改成英文
"""
import pandas as pd

# 1. 将以上的数据存入一个名为df的DataFrame对象中
df01 = pd.read_excel("info.xlsx")
# print(df01)

# 2. 显示前5行数据
# print(df01.head())

# 3. 查看第1、3、5行中第2、4、6列的数据
# print(df01.iloc[[0, 2, 4], [1, 3, 5]])

# 4. 显示李四销售化妆品的情况
# print(df01[(df01["姓名"] == "李四") & (df01["柜台"] == "化妆品")])

# 5. 统计张三的上班次数
# df02 = df01[df01["姓名"] == "张三"]
# df02 = df02.drop_duplicates(subset=["日期"])
# c = df02.count()["姓名"]
# print(c)

# 6. 将表头由中文改成英文
# 使用columns修改列名的时候需要长度匹配
# df01.columns = ["eid", "name", "date", "time", "money", "counter"]
df02 = df01.rename({"工号": "eid"}, axis=1)
print(df02)
