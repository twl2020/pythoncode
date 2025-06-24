"""
可变形参注意点:
可变关键字参数必须定义在普通参数之后
可变位置参数可以在普通参数(keyword-only)之前或之后
可变位置参数和可变关键字参数同时存在是,可变位置参数必须在可变关键字参数之前

"""
def fun(a, **kwargs):
    print(a, kwargs)


# 记住：可变关键字参数就是最末端了
def fun01(*args, **kwargs):
    print(args, kwargs)


def fun02(a, *args):
    print(a, args)


def fun03(*args, a):
    print(a, args)


fun(10)
fun01(1, 2, 3, a=10)

fun02(10, 11, 12)
fun03(10, 11, 12, a=13)
