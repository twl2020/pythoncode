"""
在定义形参的时候 / 前面的参数就是positional-only参数
positional-only参数： 只能通过位置传参的方式传入

"""


def out(a, b, /):
    print(a, b)


def out01(a, /, b):
    print(a, b)


out(1, 3)
# out(a=1, b=3)
out01(10, b=20)
out01(10, 200)

sum()
