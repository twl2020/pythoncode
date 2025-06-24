"""
可调用对象： 这个知识点很重要， 后面大家学习深度学习模型的时候， pytorch框架底层基本上都是用可调用对象

可调用对象(callable object)： 就是可以直接在 对象名后面添加() 调用对应的功能
可调用对象： 对象名()

python中函数就是可调用对象

可调用对象必须实现 __call__()魔术方法， 才能成为可调用对象
"""


class Cat:

    def eat(self, food):
        print("吃啥呢", food)

    def __call__(self, *args, **kwargs):
        self.eat(kwargs)


cat = Cat()
cat(food="🐟")
