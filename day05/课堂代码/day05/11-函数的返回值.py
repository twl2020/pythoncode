"""
函数的返回值：
  作用： 1. 返回函数的执行完成后的结果  2. 结束函数

细化的知识点：
    函数使用return语句返回 返回值
    返回值: 就是函数执行完成后返回的数据
    所有函数都有返回值,如果没有return 返回值 语句,隐式返回None
    return语句不一定是函数体的最后一条语句
    return会结束方法, 所以return后的语句不会执行
    return 后面不跟返回值, 目的是结束方法, 但是会隐式返回None
    函数不能同时返回多个值， return 1, 2, 3 返回的是元组，依然是一个值
"""


def out():
    print("haha")
    return 100


x = out()  # x = 100
print(x)


def out01():
    print(1000)


y = out01()  # None
print(y)


def out03(a):
    print("开始")
    if a % 2 == 0:
        return 10
    else:
        return 1, 2, 3


z = out03(21)
print(z)


def add(a, b):
    return a + b


res = add(2, 5)
print(res)
