import pandas as pd

s1 = pd.Series([*"abcd"], index=[11, 12, 13, 14])

# 想要查看索引或者其值时，可以使用index和values属性
print(s1)
# index返回的是RangeIndex， RangeIndex是一个惰性对象
# index获取的是标签索引， 如果标签索引没有显式设置， 标签索引使用的就是位置索引
print(s1.index)
print(list(s1.index))
print(s1.values)
