"""
生成器表达式的语法：
    就是将列表推导式中的中括号换成小括号
         （操作x的表达式  for  x  in  可迭代对象）
    注意：返回的是一个生成器对象（惰性对象）

生成器对象：是一个可迭代对象iterable，也是一个迭代器，只能循环迭代一次。
迭代器可以使用next()方法进行迭代

注意：如果函数或方法中只有一个iterable参数，此时传入的生成器表达式的()可以省略

"""
list01 = [1, 2, 3, 4, 5, 6]
g1 = (i for i in list01)
print(type(g1)) # <class 'generator'>
print(g1)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))

for x in g1:
    print(x)

print("------------------------------")
for x in g1:
    print(x)


# 注意：如果函数或方法中只有一个iterable参数，此时传入的生成器表达式的()可以省略
# s1 = "-".join((str(i) for i in list01))
s1 = "-".join(str(i) for i in list01)
print(s1)
