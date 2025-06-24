"""
try ... except 语句具有可选的 else 子句，该子句如果存在，
它必须放在所有 except 子句 之后。 它适用于 try 子句 没有引发异常但又必须要执行的代码。
    try:
           发生异常的语句
    except 异常类型 as 标识符:
            捕获异常后的处理语句
    else:
           语句
    finally:
          语句

以后大家写代码的时候常用到异常的地方： 加载一些文件的时候

try:
    font = load("楷体.tf")
finally:
    font = default_font()
"""

try:
    print(6 / 0)
except ZeroDivisionError as e:
    print("e=====", e)
else:
    print("else语句的代码")
finally:
    print("====finally=====")