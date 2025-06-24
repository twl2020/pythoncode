"""
嵌套函数:
  嵌套函数（nested function），也称为内部函数，指在一个函数的定义内部又定义了另一个函数。
"""

# 嵌套函数
def out():
    x = 10
    def show():
        print("show......", x)

    return show

f = out()
f()

out()()
