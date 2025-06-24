d1 = {"a": 100, "b": 200, "c": 88, "d": 300}

# item：元素
# items()： 获取到字典中的所有元素, 也就是所有的kv键值对
x = d1.items()
print(x)

for t in d1.items():
    print(t)

print("------------------------------")

for k, v in d1.items():
    print(k, v)

print("------------------------------")
# 直接遍历字典， 得到的是所有key
for k in d1:
    print(k)

print(d1.keys())

for k in d1.keys():
    print(k)


