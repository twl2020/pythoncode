"""
可以直接使用numpy的函数
应用函数：apply()和applymap()
排序：sort_index() 和 sort_values()

"""
import numpy as np
import pandas as pd

data = np.arange(1, 13).reshape(3, 4)
df01 = pd.DataFrame(data)
print(df01)


def func01(ele):
    return np.sum(ele)


# apply将DataFrame对应轴上的Series数据传给function函数进行操作， 然后返回结果
# df02 = df01.apply(func01, axis=1)
# df02 = df01.apply(lambda s: np.sum(s), axis=1)
df02 = df01.apply("sum", axis=1)
print(df02)
print("------------------------------------------")

def func02(e):
    return e + 3


# applymap和map 接收的DataFrame中的每一个元素， 然后交给function函数操作返回结果
# applymap该函数已经过时了， 使用map函数替换
# df03 = df01.applymap(func02)
# df03 = df01.map(func02)
df03 = df01.map(lambda e: e + 3)
print(df03)

print("------------------------------------------")
df04 = pd.DataFrame([[1, 3, 10], [0, 7, 8], [2, 1, 13]], index=[2, 0, 1])
print(df04)
# sort_index(): 排序排的是索引， 默认是0轴的索引
df05 = df04.sort_index()
print(df05)
