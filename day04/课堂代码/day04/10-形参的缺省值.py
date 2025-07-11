"""
形式参数的缺省值(默认值)：
         可以在定义函数的时候，给形式参数添加一个缺省值。缺省值参数必须在普通参数之后
格式：
   	def 函数名(参数=值): ...
作用：
形参的默认值可以在没有传入实参时候，给形参赋值
形参比较多的时候，不需要用户每次都输入所有的参数值，简化函数的调用

"""


# 缺省值参数必须在普通参数之后
# 200就是参数b的默认值
def out(a, b=100):
    print(f"a：{a}")
    print(f"b：{b}")


# 给参数b传入了实参， 会覆盖b的默认值
out(1, 3)
# 没有给参数b传入实参， b就是使用默认值
out(1)
