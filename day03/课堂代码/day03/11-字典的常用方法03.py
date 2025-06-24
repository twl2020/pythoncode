d1 = {"a": 100, "b": 200, "c": 88, "d": 300}

# 获取所有的value值
v = d1.values()
print(v)
for i in d1.values():
    print(i)

# pop: 如果key存在就删除并返回被删的元素； 否则报错或者返回指定的默认值
print("--------------------------------------")
# e = d1.pop("cc", -100)
# print(e, d1)

# d. popitem()： 从字典中移除并返回一个 (键, 值) 对。 键值对会按 LIFO 的顺序被返回。
# x = d1.popitem()
# print(x)
# x = d1.popitem()
# print(x)

# update([other])：使用来自 other 的键/值对更新字典，覆盖原有的键。 返回 None。
# Key存在就是修改，key不存在就是增加
print(d1)
d1.update({"cc": 999})
print(d1)

print("----------------------------------")
d2 = {"a": 100, "b": 200, "c": 88, "d": 300}
d3 = {"a": 1000, "b": 2000, "cc": 880, "d": 3000}

# d | other：合并 d 和 other 中的键和值来创建一个新的字典，两者必须都是字典。
# 当 d 和 other 有相同键时， other 的值优先。（Added in version 3.9）

d4 = d2 | d3
print(d2)
print(d3)
print(d4)

print("----------------------------------")
# d |= other：用 other 的键和值更新字典 d 。当 d 和 other 有相同键时， other 的值优先。
# 就地修改（Added in version 3.9）
d2 = {"a": 100, "b": 200, "c": 88, "d": 300}
d3 = {"a": 1000, "b": 2000, "cc": 880, "d": 3000}
d2 |= d3  # d2 = d2 | d3
print(d2)


