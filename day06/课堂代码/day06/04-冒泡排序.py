list01 = [10, 1, 7, 4, 6, 2]

# 第一次比较：
for j in range(len(list01) - 1 - 0):
    if list01[j] > list01[j + 1]:
        list01[j], list01[j + 1] = list01[j + 1], list01[j]

print(list01)

# 第二次比较：
for j in range(len(list01) - 1 - 1):
    if list01[j] > list01[j + 1]:
        list01[j], list01[j + 1] = list01[j + 1], list01[j]

print(list01)

# 第三次比较：
for j in range(len(list01) - 1 - 2):
    if list01[j] > list01[j + 1]:
        list01[j], list01[j + 1] = list01[j + 1], list01[j]

print(list01)

# 第四次比较：
for j in range(len(list01) - 1 - 3):
    if list01[j] > list01[j + 1]:
        list01[j], list01[j + 1] = list01[j + 1], list01[j]

print(list01)

# 第五次比较：
for j in range(len(list01) - 1 - 4):
    if list01[j] > list01[j + 1]:
        list01[j], list01[j + 1] = list01[j + 1], list01[j]

print(list01)


print("------------------------------")

list01 = [10, 3, 7, 4, 6, 2]
for i in range(len(list01) - 1):
    for j in range(len(list01) - 1 - i):
        if list01[j] > list01[j + 1]:
            list01[j], list01[j + 1] = list01[j + 1], list01[j]


print(list01)

