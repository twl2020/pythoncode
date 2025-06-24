"""
__len__():  当使用len()函数的时候其实底层调用的就是__len__()
__del__():  当使用垃圾回收器回收对象的时候调用的就是__del__()
__getitem__(): 当使用索引访问元素的时候调用的就是__getitem__()
__setitem__(): 当使用索引给元素赋值的时候调用的就是__setitem__()
__delitem__(): 当使用索引删除元素的时候调用的就是__delitem__()

"""

# 自定义的容器， 底层数据结构： 列表
class MyList:

    def __init__(self):
        self.__contanier = []

    def __getitem__(self, index):
        print("使用索引访问了", index)
        return self.__contanier[index]

    def __setitem__(self, index, value):
        self.__contanier[index] = value


    def append(self, ele):
        self.__contanier.append(ele)

    def remove(self, ele):
        self.__contanier.remove(ele)

    def __len__(self):
        return 100

    def __str__(self):
        return str(self.__contanier)

    def __del__(self):
        print("哈哈")


list01 = MyList()
list01.append(1)
list01.append(10)
list01.append(100)
list01.append(1000)
print(list01)
list01.remove(100)
print(list01)
list01[0] = 999
e = list01[0]
print(e)
print(list01[2])