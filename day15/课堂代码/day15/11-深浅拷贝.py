
# copy() 函数是浅拷贝
# python中不可变数据类型的数据做深拷贝是没有意义（因为和浅拷贝效果一样）
list01 = [[1], 2, 3, 4, 5, 6]
list02 = list01.copy()
print(list01)
print(list02)
list02[0][0] = 100
print(list01)
print(list02)

print("-----------------------------------")

# 深拷贝
import copy

list01 = [[1], 2, 3, 4, 5, 6]
list02 = copy.deepcopy(list01)
print(list01)
print(list02)
list02[0][0] = 100
print(list01)
print(list02)

