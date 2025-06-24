class Cat:
    a = 100

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age


cat1 = Cat("大花猫", "花色", 2)
cat2 = Cat("小花猫", "花色", 1)

print(cat1.name)
print(cat2.name)
print(cat1.__dict__)  # 查看对象的成员属性
print(vars(cat1)) # 查看对象的成员属性, vars返回的就是__dict__的结果
print(Cat.__dict__)  # 查看类的类属性

