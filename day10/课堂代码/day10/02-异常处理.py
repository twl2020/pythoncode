"""
捕获异常：
  1. 找到可能出现异常的代码
  2. 将该代码使用 try...except 包裹起来

捕获异常语法：
   try:
      可能出现异常的代码
   except 异常类型 as 变量名:    ---  这里的变量名就是用来接收异常信息的
       处理异常的代码
   except 异常类型 as 变量名:
       处理异常的代码
   finally:
       资源释放的代码


注意： try中发生异常语句后面的代码也不会执行

finally： 最终的意思
finally在异常的执行效果是: 不管try的代码是否发生异常， finally中的代码都会执行
finally的作用： 常用于资源的释放
"""

print("start----------")
a = 10
b = 2
try:
    print(a / b)
    print("hello" + a)
    # print(int("a"))
    # print([10][2])
except ZeroDivisionError as e:
    print("出现异常了", e)
except TypeError as e:
    print("e==>", e)
except (ValueError, IndexError) as e:
    print("错误", e)
finally:
    print("finally-----")

print("end----------")
