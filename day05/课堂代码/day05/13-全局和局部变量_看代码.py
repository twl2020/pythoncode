

"""
global: 全局的意思
作用: 将函数中的变量声明为全局变量
建议: 一般不使用global, 会破坏函数的封装, 如果要使用全局的变量,建议使用参数的方式传递

"""

# python中 赋值即定义
x = 1
def show():
    global x
    x = x + 1
    print(x)

    global y
    y = 100


def out(x):
    x = x + 1
    print(x)

show()
print(x)
print(y)

out(x)