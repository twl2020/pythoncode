class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("大花猫", 2)
cat2 = Cat("小花猫", 1)
cats = [cat1, cat2]

name = input("请输入name:")
age = int(input("请输入age:"))
for cat in cats:
    new_cat = Cat(name, age)
    if cat.name == name:
        cat = new_cat

for cat in cats:
    print(cat.name, cat.age)