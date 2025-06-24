class Cat:
    num = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_num(cls, fish_num):
        if fish_num > 0:
            cls.num = fish_num

    @classmethod
    def get_cat(cls, name, age):
        return cls(name, age)

    def eat(self):
        print(f"{self.name}吃了{self.num}条🐟")


Cat.set_num(3)
# 创建对象  -- 使用构造函数初始化数据
cat = Cat("波斯猫", 2)
cat.eat()

# 创建对象  -- 使用工厂方法创建对象
cat = Cat.get_cat("大花猫", 1)
cat.eat()
