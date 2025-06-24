"""
match 语句接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较。
只有第一个匹配的模式会被执行，并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量。
match 和 case 是 soft keywords 。

模式匹配和if语句有相似之处： 每个条件直接都是互斥的； 但是模式匹配比if语句更加的强大。
"""

# 使用模式匹配完成字面值的比较
status = 700
match status:
    case 200:
        print("网络正常")
    case 404:
        print("资源错误")
    case 500:
        print("服务器内部错误")
    # case后面跟变量 相当于if中的else, 写在最后, 这个变量是接收不满足其他条件的值
    # case后面跟_ 相当于if中的else, 写在最后,只是这个不满足其他条件的值我们也不使用
    case x:
        print("未知错误", x)
    # case _:
    #     print("未知错误")



# if status == 200:
#     print("网络正常")
# elif status == 404:
#     print("资源错误")
# elif status == 500:
#     print("服务器内部错误")
# else:
#     print("未知错误")