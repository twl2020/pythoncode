"""
3. 使用lambda和三目运算符实现两个数据ab比大小，谁大返回谁
"""
x = 10
y = 20
f = lambda a, b: a if a > b else b
m = f(x, y)
print(m)
