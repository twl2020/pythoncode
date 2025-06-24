"""
多态： 多种形态
class Pet:

class Dog(Pet):

class Cat(Pet):


Python中并没有明确的说明多态. 所以我们只需要掌握封装和继承即可

"""


class Pet:
    def eat(self):
        print("吃东西")


class Cat(Pet):
    def eat(self):
        print("吃鱼")


class Dog(Pet):
    def eat(self):
        print("啃骨头")


class Person:
    # 喂养宠物
    def feed(self, pet: Pet):
        pet.eat()


person = Person()
person.feed(Cat())
person.feed(Dog())
