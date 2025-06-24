def xxx(x):
    return x[1]


list01 = [("a", 3), ("b", 2), ("c", 1)]
# list01.sort(key=xxx)
list01.sort(key=lambda x: x[1])
print(list01)


list02 = ["1", "11", "101"]
# list02.sort(key=lambda x: int(x))
list02.sort(key=int)
print(list02)
