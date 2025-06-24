"""
学习异常掌握两个内容：
1. 出现了异常怎么处理
2. 怎么抛出错误信息

程序中的异常都继承自 Exception即可

Error:  语法错位
Exception: 程序解析是没有问题， 但是执行的过程中可能会出现问题
"""

# print("a" + 10)  # TypeError
# print(int("a"))  # ValueError
# print([10][3])  # IndexError

# StopIteration
# g = (a for a in range(3))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # StopIteration

print(1 / 0)  # ZeroDivisionError
print("over-----")
