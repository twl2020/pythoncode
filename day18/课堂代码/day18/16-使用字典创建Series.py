"""
方式四：使用字典创建Series

在pandas中 NaN 表示缺失值
"""
import pandas as pd

d = {
    "id": 1001,
    "name": "张三",
    "age": 26,
    "sex": "male"
}

"""
通过字典创建Series的时候， 会自动的将字典的key作为标签索引
此时通过index设置标签索引的时候，index中的值是key， 值就会显示， 否则值就是NaN
此时index中元素的个数可以是数据长度不一致

在pandas中 NaN 表示缺失值
"""
s1 = pd.Series(data=d, dtype="O", name="用户信息", index=["id", "name", "age", "sex", "score"])
print(s1)