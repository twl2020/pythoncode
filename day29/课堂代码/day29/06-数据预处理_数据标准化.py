"""
数据标准化处理： preprocessing.StandardScaler
"""
import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[100, 10, 78], [1, 1999, 3]])

# 标准化处理
scaler = StandardScaler()
# 调用fit, 得到均值和方差
scaler.fit(X)
# print(scaler.mean_)
# print(scaler.var_)
y = scaler.transform(X)
print(y)
print(y.mean())  # 获取标准化后的均值
print(y.var())  # 获取标准化后的方差
print(y.std())  # 获取标准化后的标准差

# 将标准化后的数据转成原始的特征数据
z = scaler.inverse_transform(y)
print(z)
