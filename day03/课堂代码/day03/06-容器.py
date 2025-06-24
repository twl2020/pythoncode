list01 = [1, 3, 4, 5, 3, 6]
i = list01.index(3, 2)
print(i)

t1 = 1,
print(t1)

# 索引: 单个元素
# 切片： 一个范围的元素, 返回的是一个新的容器对象
# start --> stop 的方向 必须和 step的方向一致
list01 = [1, 2, 3, 4, 5, 6, 7]
print(list01[:3])  # [1, 2, 3]
print(list01[2:5])  # [3, 4, 5]
print(list01[:])  # [1, 2, 3, 4, 5, 6, 7]
print(list01[-3:-1])  # [5, 6]
print(list01[-1:-3:-1])  # [7, 6]
print(list01[0:-3:-1])  # []
