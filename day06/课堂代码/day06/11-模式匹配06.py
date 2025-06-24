"""
模式守卫:
   case 语句后面的 if语句就是模式守卫
"""
point = eval(input("请输入坐标："))
match point:
    case [0, 0]:
        print("原点")
    case (x, 0) if x > 10:
        print("这是x轴上的一个点", x)
    case (x, y):
        print("这是x和y组成的一个点")
    case _:
        print("这是一个坐标点")