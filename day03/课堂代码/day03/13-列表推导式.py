list01 = [1, 2, 3, 4, 5, 6]

# 需求： 将列表中的元素+1得到一个新的列表
list02 = []
for i in list01:
    list02.append(i + 1)

print(list02)

print("-------------------------------")
# 列表推导式语法： 列表变量 = [操作x的表达式  for  x  in  可迭代对象]
list03 = [i + 1 for i in list01]
print(list03)

print("-------------------------------")
# 需求： 将list01中的偶数存储成一个新的列表
# list04 = []
# for i in list01:
#     if i % 2 == 0:
#         list04.append(i)
# print(list04)

list04 = [i for i in list01 if i % 2 == 0]
print(list04)


# list04 = [i+j for i in list01 for j in list01]
# print(list04)
