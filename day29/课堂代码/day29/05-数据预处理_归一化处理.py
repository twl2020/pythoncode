"""
在sklearn当中，我们使⽤preprocessing.MinMaxScaler来实现这个功能。

sklearn预处理的步骤：
1. 创建对应的预处理类的对象
2. 调用fit， 得到预处理过程中算法需要使用的值
3. 调用transform， 做预处理

以上的步骤2和3可以合二为一：fit_transform()
"""
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 一般都是使用大写的X表示特征
# 在sklearn中特征必须是二维的， 因为可以同时处理多个样本数据
# 所以X的形状是： (n_samples, n_features)
X = np.array([[1, 2, 3], [4, 5, 6], [1000, 89, 3]])

# 对X进行归一化, 默认是将特征数据归一化到: 0-1
scaler = MinMaxScaler()
# scaler = MinMaxScaler(feature_range=(1, 5))
# 调用fit函数, 计算出最大值和最小值， 方便后面transform进行归一化处理
# scaler.fit(X)
# print(scaler.data_min_)
# print(scaler.data_max_)
# 调用transform， 进行归一化处理
# y = scaler.transform(X)

y = scaler.fit_transform(X)
print(y)
print("-------------------------------")
# 将归一化后的数据转成原始的特征数据
z = scaler.inverse_transform(y)
print(z)
