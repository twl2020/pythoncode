"""
思考： 在类中定义一个无参方法， 是否可以？？？
      1. 普通的无参是不可以的
      2. 静态方法定义成无参是可以的。
因为： 静态方法使用了装饰器，不会进行绑定，也就不会注入第一个参数，此时方法可以是无参方法，也就是不会隐式的注入参数


python中被 @staticmethod 修饰的方法就是 静态方法

普通方法和静态方法：
1. 普通方法使用时， 必须先创建了对象才能使用
     对象.普通方法()
     类.普通方法(对象)
2. 静态方法时候时， 无需创建对象即可使用   -- 随着类的加载就加载了， 所以有了类静态方法就可以使用了
     类.静态方法()
     对象.静态方法()
3. 静态方法也是可以带参数的， 但是里面的参数都是传入的值，不会像普通函数一样将第一个参数当作传入的对象


静态方法的使用场景： 定义工具类中方法就使用静态方法
"""


class Cat:

    def __init__(self):
        pass

    @staticmethod
    def eat():
        print("吃🐟")

    def sleep(self):
        print("睡觉觉")

    @staticmethod
    def run(addr):
        print(f"🐟在{addr}游")


cat = Cat()
print(cat.eat)  # <function Cat.eat at 0x000001621DADB5B0>
print(Cat.eat)  # <function Cat.eat at 0x000001621DADB5B0>

cat.eat()
Cat.eat()

print("------------------------------------------")
Cat.eat()
cat.eat()
Cat.run("太平洋")

