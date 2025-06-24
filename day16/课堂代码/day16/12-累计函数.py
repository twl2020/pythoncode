"""
np.add.accumulate(): 累计求和
np.subtract.accumulate(): 累计求差
np.multiply.accumulate()： 累计求乘
np.divide.accumulate()：累计求除
np.mod.accumulate()：累计求模
np.minimum.accumulate()： 累计计算最小值
np.maximum.accumulate()： 累计计算最大值

累计函数： 每个元素都会进行一次累计运算
"""
import numpy as np

np.random.seed(0)
a = np.arange(1, 11)
np.random.shuffle(a)
# b = np.add.accumulate(a)
b = np.maximum.accumulate(a)
print(a)
print(b)