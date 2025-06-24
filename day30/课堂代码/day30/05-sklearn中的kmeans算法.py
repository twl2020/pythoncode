"""
k-means是一种聚类算法， 属于非监督学习
聚类： 事先不知道数据的类别
"""
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# random_state的作用就是固定随机数的种子， 以便固定样本数据
data = make_blobs(random_state=0)
# 模拟得到的特征数据， 这些特征数据我们实现不知道类别
X = data[0]

print(X)

# 可视化
# plt.scatter(X[:, 0], X[:, 1])
# plt.scatter(X[:, 0], X[:, 1], c=data[1])

# 创建对象
# random_state: 表示固定住初始质心
# n_clusters: 表示将数据聚类成几个类（簇）
kmeans = KMeans(n_clusters=3, random_state=10)
kmeans.fit(X)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)

plt.show()
