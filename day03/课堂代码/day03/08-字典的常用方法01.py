

# dict.fromkeys(iterable, value=None, /)
d0 = dict.fromkeys(range(5))
print(d0)

d1 = {"a": 100, "b": 200, "c": 88, "d": 300}
# d1["c"]： 获取key为c时候对应的value, key不存在会报错
print(d1["c"])
# 修改key为c时候对应的value
d1["c"] = 111
print(d1["c"])

# Signature: d.get(key, default=None, /)
# Return the value for key if key is in the dictionary, else default.
v = d1.get("cc", -1)
print(v)

print(f"删除前{d1}", id(d1))

del d1["c"]

print(f"删除后{d1}", id(d1))

# d.clear()：移除字典中的所有元素。
d1.clear()
print(d1)

