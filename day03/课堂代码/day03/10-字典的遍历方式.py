d1 = {"a": 100, "b": 200, "c": 88, "d": 300}

# 遍历方式1
for k, v in d1.items():
    print(k, v)


# 遍历方式2
for k in d1:
    print(k, d1[k])

# 遍历方式3
for k in d1.keys():
    print(k, d1[k])
