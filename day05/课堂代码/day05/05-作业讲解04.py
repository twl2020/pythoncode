"""
6. 求阶乘 n! = 1 * 2 * 3 * 4 * ..... * n
"""


def factorial(n):
    if n < 0:
        return NotImplemented
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


res = factorial(-5)
print(res)
