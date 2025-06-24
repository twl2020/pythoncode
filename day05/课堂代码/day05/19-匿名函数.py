"""
匿名函数：没有名字的函数

Python中使用lambda表达式构建匿名函数

匿名函数的使用场景： 用作参数传递

Lambda表达式也叫做单行函数
lambda表达式的语法：
      lambda 参数 : 函数体
说明：
    1. 参数不能带(),多个参数使用逗号分隔
    2. 没有参数的时候，冒号前面就空着
    3. 函数体中不能出现 = 和 return
    4. Lamda表达式只能写在一行
"""


def f1():
    print("哈哈")


def f2(x):
    print("哈哈", x)


def add(a, b):
    return a + b


f1()

# 使用lambda改进f1
x = lambda: print("哈哈")
x()

x = lambda a: print("哈哈", a)
x(10)

res = lambda a, b: a + b
print(res(3, 5))
