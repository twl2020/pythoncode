"""
raise 语句支持强制触发指定的异常
语法：
   raise [异常]

"""


# class FactorialError(Exception):
#     def __init__(self, message):
#         super().__init__(message)


# class FactorialError(Exception): pass
class FactorialError(Exception): ...


def factorial(n):
    if n < 0:
        # 抛出异常  -- 手动触发异常
        # raise Exception("负数是没有阶乘的")
        raise FactorialError("负数是没有阶乘的")

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(-5))
