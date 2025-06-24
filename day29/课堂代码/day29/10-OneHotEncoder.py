"""
OneHotEncoder:
  特征专⽤，能够将分类特征转换为分类数值
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("resources/titanic_train.csv")

# 获取 Sex 和 Embarked
X = df.loc[:, ["Sex", "Embarked"]]
# print(X)


encoder = OneHotEncoder()
encoder.fit(X)
# print(encoder.categories_)
X_ = encoder.transform(X)  # 将字符类型的特征转成数值
arr = X_.toarray()
print(arr)

print(encoder.get_feature_names_out())