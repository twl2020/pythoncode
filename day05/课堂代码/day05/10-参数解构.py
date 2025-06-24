"""
参数解构：
 1. 调用方法时, 在实参(可迭代对象)前面添加 * 表示参数解构(解构成位置传参)
 2. 实参是字典的时候, * 解构key , **解构出来key-value(解构成关键字传参)

"""


def out(a, b):
    print(a, b)


def show(name, age):
    print(name, age)


out(1, 2)

t1 = (11, 12)
out(*t1)

# 封包
t2 = 20, 30
out(*t2)

t3 = [100, 200]
out(*t3)

t4 = "xy"
out(*t4)

t5 = {"name": "张三", "age": 20}
out(*t5)
# out(**t5) ==> out(name="张三", age=20)
# **解构实参的时候， 实参的key值必须是形参的名称
# out(**t5)
show(**t5)