"""
模式匹配： 类似于解包的方式， 绑定变量
"""
# 注意：这种方式match case 不会区分数据类型，(),[]都是一样的
point = eval(input("请输入坐标："))
match point:
    case [0, 0]:
        print("原点")
    case (x, 0):
        print("这是x轴上的一个点", x)
    case (0, _):
        print("这是y轴上的一个点")
    case (x, y):
        print("这是x和y组成的一个点")
    case _:
        print("这是一个坐标点")
