"""
变量名解析原则：LEGB
L: Local  本地变量
E: Enclosing 外层函数中的变量
G: Global 全局变量
B: Build-in 内置变量
"""

max = 1
a = 1
def out():
    max = 2
    print(a)
    def show():
        max = 3
        print(max)
    show()

out()
