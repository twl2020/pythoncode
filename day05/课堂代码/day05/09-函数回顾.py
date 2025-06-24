"""
函数的参数：
  1. 形式参数： 定义函数的时候， 函数名()中的参数就是形参
     a. 普通参数   def show(a, b)
     b. 参数的默认值  def show(a=10, b=10)  或者 def show(a, b=10)
         普通参数要在关键字参数前面
     c. 可变位置参数  def show(*args) 或者 def show(a, *args) 或者 def show(a, *args, b)
       *后面跟上标识符， 就是可变位置参数， 会将接收到的数据封装成 tuple
       可变位置参数 可以接收0或多个实际参数
     d. 可变关键字参数  def show(**kwargs) 或者 def show(a, ***kwargs) 或者 def show(a, *args, **kwargs)
        **后面跟标识符， 就是可变关键字参数
        可变关键字参数只能在参数的最末端
        可变关键字参数接收0或多个实际参数， 将接收的参数成dict
     e. keyword-only参数
        形参列表中， * 或者 可变位置参数 后面的参数就是keyword-only参数
        keyword-only参数传入实参的时候必须通过关键字传参
     f. positional-only参数
       形参列表中， / 前面的参数就是positional-only参数
       positional-only参数传入实参的时候必须通过位置参数

  2. 实际参数： 调用函数的时候， 函数名()中的参数就是实参
     - 位置传参
     - 关键字传参
     普通形参可以使用位置传参或关键字传参
     keyword-only参数只能是关键字传参
     positional-only参数只能是位置传参
"""


