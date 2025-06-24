import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("resources/titanic_train.csv")

# 将最后一列分类标签由 Yes和No 转成数字
# 先获取最后一列数据
label = df.iloc[:, -1]
print(label)

# 注意： 特征要求是二维； 现在处理的是label标签， 是一维的
encode = LabelEncoder()
encode.fit(label)
print(encode.classes_)  # 获取类别
label_digit = encode.transform(label)
print(label_digit)
