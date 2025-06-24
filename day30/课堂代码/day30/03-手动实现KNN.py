"""
KNN的⼯作原理：给定⼀个已知标签类别的训练数据集，输⼊没有标签的新数据后，在训练数
据集中找到与新数据最邻近的k个实例，如果这k个实例的多数属于某个类别，那么新数据就属
于这个类别。
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# 创建10个样本的二维特征
data = np.array([
    [3, 7.9],
    [1.2, 11.9],
    [3.4, 6],
    [1, 8.9],
    [2.3, 6.9],
    [1.5, 4.9],
    [3.1, 7.9],
    [2.3, 9],
    [4.5, 9.9],
    [3.8, 4.9],
])

# 十个样本数据的已知标签
labels = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# 定义一个未知类型的特征数据
data_new = np.array([[3, 5]])

# 先完成数据的可视化， 方便观察
# 已知数据的第一个特征作为x轴， 第二个特征作为y轴; 同时还需要区分出不同的类别
# 获取0类别的数据
data_0 = data[labels == 0]
# 获取1类别的数据
data_1 = data[labels == 1]

# 绘制0类别的数据
plt.scatter(data_0[:, 0], data_0[:, 1], color="red")
# 绘制1类别的数据
plt.scatter(data_1[:, 0], data_1[:, 1], color="blue", marker="^")
# 绘制未知数据
plt.scatter(data_new[:, 0], data_new[:, 1], marker="+")

# 接下来使用KNN算法， 预测出未知数据data_new属于哪一种类别
# 1. 计算已知特征数据和未知数据之间的欧式距离
distances = np.array([np.linalg.norm(X - data_new) for X in data])

# 2. 将distances进行升序的时候不能直接将距离值升序， 而是应该得到排序后的索引
# 这样做的目的时为了保证 distances的索引和特征数据的索引是一一对应的
distance_index = distances.argsort()
print(distance_index)
# 3. 选择k个最近的邻居
k = 3
neighbour = distance_index[:k]
print(neighbour)
# 4. 根据最近的邻居的索引取出对应的标签
target = labels[neighbour]
print(target)
# 5. 对类别进行次数统计
# 1: 表示获取次数最多的一个
counter = Counter(target).most_common(1)
result_label = counter[0][0]
print(result_label)

plt.show()
