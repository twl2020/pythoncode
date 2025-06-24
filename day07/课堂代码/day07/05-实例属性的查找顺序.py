class Dog:
    name = "小狗狗"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog("旺财", 2)
print(dog.name)
# var() 就是查看__dict__的内容
print(dog.__dict__)  # {'name': '旺财', 'age': 2}
print(dog.__class__)  # <class '__main__.Dog'>
print(Dog.__dict__)  # {'name': '小狗狗'}

