# 数字类型  --- 不可变的数据类型
# 整型：int， 表示所有的整数
# 布尔型：bool, 只有True和False
# 布尔型是整型的子类型： 非0就是True; 0是False
# 浮点型：float 所有的小数
# 复数: complex

a = 10
a = 11
print(a)

# 序列：
# 可变序列：
# 不可变序列：str, tuple, range
# range: 表示的一个范围， 惰性对象
# 惰性对象: 只有使用的时候才会加载

# 可变序列： list
# list的底层是  顺序表
# 顺序表： 在内存中是一段连续的地址空间

# 映射类型： python中的映射类型有且只有一个  就是  字典dict
# 集合类型： set, 可变的数据类型, 无序，元素唯一
# set的底层是哈希表
# 无序： 元素迭代的顺序无法保证始终和插入数据的顺序一致。
# 哪些类型的数据可以存储在set集合中
# 可哈希的数据类型才能存储在set中
# 不可变的数据类型  可哈希


# r = range(10)
# print(r)  # range(0, 10)
#
# for x in range(10):
#     print(x)
#
set01 = {"a", "b", "c", "d"}
print(set01)

list01 = [1, 3, 5, 7]
print(id(list01), id(list01[1]), list01)
list01[1] = 88
print(id(list01), id(list01[1]), list01)

print(hash(10))
print(hash("a"))

# 0-5
#
# print(hash("a") % 6)
print(hash("a") & 5)

i = NotImplemented
print(i)


def xxx(age):
    if (age < 0):
        return NotImplemented


e = ...
print(e)

if True:
    ...