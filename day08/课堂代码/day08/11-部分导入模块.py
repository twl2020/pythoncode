"""
部分导入语句：
    部分导入：from 模块 import …
    设置别名：from 模块 import … as…

部分导入不会将模块名添加到命名空间中， 所以不能使用模块名
部分导入将模块名中导入的内容的名称添加到命名空间中， 所以可以直接时殷弘模块内容的名字
"""
# from utils import num, add, A
# print(num)
# print(add)
# print(A)


from utils import num as n, add as a, sub
print(n)
print(a)
print(sub.xx)