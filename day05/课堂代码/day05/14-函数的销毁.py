"""
函数的销毁：
    定义一个函数就是生成一个函数对象，函数名指向这个函数对象(内存空间)
    可以使用del语句删除函数
    函数执行完，没有被引用会被销毁
"""

# a = 10
# del a
# print(a)


def show():
    print("hello")

show()


del show
show()