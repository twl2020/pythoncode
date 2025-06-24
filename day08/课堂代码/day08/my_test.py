def add(a, b):
    print(a, b)


def show(info):
    print(f"info={info}")


# 测试代码
if __name__ == '__main__':
    add(2, 5)
    show("hello")
    print(f"模块的名称是：{__name__}")
