"""
工具类： 要求开箱即用（不用创建对象就可以直接使用方法）， 就会将方法定义成静态， 方便直接调用
"""
class Calc:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def sub(a: int, b: int) -> int:
        return a - b


print(Calc.add(1, 3))
