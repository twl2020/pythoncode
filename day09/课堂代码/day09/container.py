"""
2. 自定义容器， 具备以下功能：
    a. 可以使用索引操作
    b. 具备增删查改的功能
    c. 打印容器对象的时候输出元素内容

分析：
   1. 自定义容器，底层使用什么数据结构？？？
        需要用到索引， 我们可以采用 list列表
   2. [索引]操作的时候需要涉及到哪些魔术方法？？
       __setitem__()：   list01[index] = xxx
       __getitem__():    a = list01[index]
       __delitem__():    del list01[index]
   3. 增删查改的功能
      增：append(value)
      删：remove(value)  或者 del list01[index]
      查：index(value)   或 list01[index]
      改：list01[index] = xxx
   4. 打印容器对象的时候输出元素内容
       __repr__()

"""


class MyList:
    def __init__(self):
        # 自定义容器底层采用的数据结构
        self.__data = []

    def __setitem__(self, index, value):
        # __setitem__()：   list01[index] = xxx
        self.__data[index] = value

    def __getitem__(self, index):
        # __getitem__():    a = list01[index]
        return self.__data[index]

    # 如果没有重写__iter__魔术方法， for循环迭代的时候调用的是__getitem__
    def __iter__(self):
        return iter(self.__data)

    def __delitem__(self, index):
        # del list01[index]
        del self.__data[index]

    def __len__(self):
        return len(self.__data)

    def append(self, value):
        self.__data.append(value)

    def remove(self, value):
        self.__data.remove(value)

    def index(self, value):
        return self.__data.index(value)

    def __repr__(self):
        return repr(self.__data)


if __name__ == '__main__':
    list01 = MyList()
    list01.append(1)
    list01.append(11)
    list01.append(111)
    print(list01)
    # list01[0] = 100
    # print(list01)
    # print(list01[1])
    # del list01[1]
    # print(list01)

    # for i in list01:
    #     print(i)

    list01.remove(1)
    print(list01)

    print(list01.index(11))




