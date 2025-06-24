"""
OrdinalEncoder:
  特征专⽤，能够将分类特征转换为分类数值
"""

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("resources/titanic_train.csv")

# 获取 Sex 和 Embarked
X = df.loc[:, ["Sex", "Embarked"]]
print(X)

encoder = OrdinalEncoder()
encoder.fit(X)
print(encoder.categories_)  # 获取特征的类别
X_ = encoder.transform(X)  # 将字符类型的特征转成数值
# print(X_)
df.loc[:, ["Sex", "Embarked"]] = X_
print(df)
