import sub

num = 10


_age = 18

# __all__的元素必须是字符串， 也就是内容的名称
__all__ = ["_age", "num", "A", "sub"]

def add(a, b):
    print(a + b)


class A:

    def show(self):
        print("A类的show方法")


