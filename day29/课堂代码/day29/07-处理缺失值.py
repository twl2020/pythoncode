import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv("resources/titanic_train.csv")
# print(df)
# print(df.info())

# 获取age的数据
s1 = df["Age"]
# print(s1)

# 通过Series得到ndarray
X = s1.values
# 特征数据要求是二维， 所以需要改变形状
X = X.reshape((-1, 1))
# print(X.shape)

# 将Age的缺失值进行填充, 默认使用均值填充
imputer = SimpleImputer()
# imputer = SimpleImputer(strategy="constant", fill_value=30)
# 接收的特征数据要求是二维的
imputer.fit(X)
age = imputer.transform(X)
# print(age)

# 将填充了缺失值的age更新df
# df["Age"] = age
df.loc[:, "Age"] = age
print(df.info())