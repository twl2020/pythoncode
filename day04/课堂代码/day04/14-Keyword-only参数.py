"""
定义函数的时候 * 或者 可变位置参数后面的普通参数叫做 keyword-only参数
Keyword-only参数只能通过关键字传参

"""


def out01(*a, b):
    print(a, b)


def out02(a, *, b):
    print(a, b)


out01(1, b=3)
out02(100, b=1)
out02(a=1000, b=1)
