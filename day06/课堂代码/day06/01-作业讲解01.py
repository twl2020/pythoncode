"""
2. 使用sorted函数实现字典的排序， 要求使用lambda的方式完成
     - 按照key排序
     - 按照value排序
"""

d1 = {"a": 100, "c": 55, "b": 79, "d": 33}

# 按照key排序
# items()得到的是kv， 没有给出key函数，默认即使按照k升序
# list01 = sorted(d1.items())
list01 = sorted(d1.items(), key=lambda x: x[0])
# ctrl + p: 查看的函数的形参
print(dict(list01))

# 按照value排序
list02 = sorted(d1.items(), key=lambda x: x[1])
print(dict(list02))