"""
numpy中提供了函数和方法

函数： np.函数()
方法： 数组对象.方法()
"""
import numpy as np

list01 = [1, 2, 3, 4, 5, 0]

arr = np.array(list01)

# 数据类型转换
arr = arr.astype("f4")
print(arr, arr.dtype)

print("--------------------------------------")
# 查看 api的详细信息
# help(np.array)
# np.info(np.array)
np.info(arr.astype)