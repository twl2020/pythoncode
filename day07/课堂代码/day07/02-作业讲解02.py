"""
2、使用面向对象完成名片管理系统  -- V1.0版本， 该版本仅仅是将名片封装成了类

名片管理 系统 录入三张名片即可

需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字
典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.


分析：
   凡是使用面向对象的思想进行编程， 一定根据需求先得到对象
   如何根据需求获取对象？？？？   使用名词提取法

查找名词： 名片  用户  姓名  电话  职位  地址
筛选名词： 名片  姓名  电话  职位  地址
哪些名词是对象， 哪些名词是属性？？
名片   --- 对象
姓名  电话  职位  地址 --- 对象的属性

有了对象名词后， 就可以创建class


for循环： 连续出现的重复代码
函数： 解决重复代码, 函数中是一些实现功能的语句
类： 解决重复代码， 类可以是任意代码（变量， 函数）
"""
class Card:
    def __init__(self, name, tel, job, addr):
        self.name = name
        self.tel = tel
        self.job = job
        self.addr = addr


# 存储名片信息的盒子
cards = []
print("欢迎进入真术名片管理系统".center(30, "*"))


def add_card():
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    job = input("请输入职位：")
    addr = input("请输入地址：")
    card = Card(name, tel, job, addr)
    cards.append(card)


def show_card():
    for card in cards:
        print(f"name:{card.name}, tel:{card.tel}, job:{card.job}, addr:{card.addr}")


def modify_card():
    name = input("请输入需要修改谁的名片：")
    # 判断名片盒子中是否存在该用户的名片
    for card in cards:
        # 说明存在该用户的名片
        if card.name == name:
            card.name = input("请输入修改后的名字：") or card.name
            card.tel = input("请输入修改后的电话：") or card.tel
            card.job = input("请输入修改后的职位：") or card.job
            card.addr = input("请输入修改后的地址：") or card.addr


def del_card():
    name = input("请输入需要删除谁的名片：")
    for card in cards:
        # 说明存在该用户的名片
        if card.name == name:
            cards.remove(card)


while True:
    print("1. 添加名片\t2.显示所有名片\t3.修改名片\t4.删除名片")
    code = input("请选择：")
    if code == "1":
        add_card()
    elif code == "2":
        show_card()
    elif code == "3":
        modify_card()
    elif code == "4":
        del_card()
    else:
        print("退出系统")
        break
