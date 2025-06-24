"""
可变形参:  就是参数的个数不固定， 可以是0个或多个
1. 可变位置参数
    在形参前面使用 * 表示该形参是可变位置参数,可以接收多个实参
    可变位置参数将接收到的实参存储在一个tuple元组中

2. 可变关键字参数
    在形参的前面使用 ** 表示该形参是可变关键字参数,可以接收多个关键字参数
    可变关键字形参将接收的实参的key和value存储在一个dict字典中

"""


# argument  参数的意思
def out(*args):
    print(args, type(args))


out(1, 2, 3)
out(1)
out()

print("---------------------------------")


def fun(**kwargs):
    print(kwargs, type(kwargs))


fun(a=1, b=2, c=3)
fun(x=1, y=2, z=3)
fun()
