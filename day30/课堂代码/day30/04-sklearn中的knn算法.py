import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

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

# 创建对象
knn_classifier = KNeighborsClassifier(n_neighbors=5)
# 将已知数据和标签交给knn训练
knn_classifier.fit(data, labels)
# 使用knn预测未知数据
pred_label = knn_classifier.predict(data_new)
print(pred_label[0])


plt.show()


