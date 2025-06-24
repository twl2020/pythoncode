"""
生成器函数: 返回生成器对象

得到生成器对象的方式有：
1. 生成器表达式  (value for x in xxx)
2. 生成器函数

生成器对象的特点：惰性的， 是可迭代的， 还是一个迭代器， 只能循环迭代一次

生成器函数：
    函数体中包含了yield语句的函数就是生成器函数，调用该方法就会返回一个生成器对象
生成器函数中可以由多次yield，每执行一次yield后就会暂停执行，把yield表达式的值返回，
再次执行会执行到下一个yield语句又会暂停执行

"""


def gen():
    yield 10
    yield 11
    yield 12
    yield 13
    yield 14


# 生成器函数返回的是生成器对象
g = gen()
print(type(g))
print(g)
# print(next(g))
# print(next(g))
# print(next(g))

for i in g:
    print(i)
