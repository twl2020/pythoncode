"""
nonlocal关键字:
 nonlocal: 将变量标记为不是本地作用域定义的变量，而是在某一层外层的局部作用域中定义，
 但不能是全局作用域中定义(也就是不会查找到全局作用域)

"""


def out():
    x = 10

    def show():
        nonlocal x
        x = x + 1
        print(x)

    show()


out()
