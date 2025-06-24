"""
使用面向对象完成名片管理系统--2.0版本

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

名词： 名片盒子  名片   姓名   电话  职位  地址
对象： 名片盒子  名片
对象的属性：
名片对象的属性： 姓名   电话  职位  地址
名片盒子对象的属性： 名片列表
名片盒子对象的功能： 增删改查
"""


class Card:
    def __init__(self, name, tel, job, addr):
        self.name = name
        self.tel = tel
        self.job = job
        self.addr = addr


# 名片盒子类： 作用完成对名片的增删改查
class CardBox:
    def __init__(self):
        # 构造函数的作用初始化对象的属性
        # 存储名片的盒子
        self.__boxes = []

    def add_card(self, card):
        # isinstance(obj, cls): 判断对象obj是不是cls类的实例
        if isinstance(card, Card):
            self.__boxes.append(card)

    def show_card(self):
        return self.__boxes

    def modify_card(self, card):
        for i, old_card in enumerate(self.__boxes):
            if old_card.name == card.name:
                card.tel = card.tel or old_card.tel
                card.job = card.job or old_card.job
                card.addr = card.addr or old_card.addr
                self.__boxes[i] = card

    def del_card(self, name):
        for card in self.__boxes:
            if card.name == name:
                self.__boxes.remove(card)


# 创建名片盒子对象
box = CardBox()
print("欢迎进入真术名片管理系统".center(30, "*"))
while True:
    print("1. 添加名片\t2.显示所有名片\t3.修改名片\t4.删除名片")
    code = input("请选择：")
    if code == "1":
        name = input("请输入姓名：")
        tel = input("请输入电话：")
        job = input("请输入职位：")
        addr = input("请输入地址：")
        card = Card(name, tel, job, addr)
        box.add_card(card)
    elif code == "2":
        boxes = box.show_card()
        for card in boxes:
            print(card.name, card.tel, card.job, card.addr)
    elif code == "3":
        name = input("请输入修改后的名字：")
        tel = input("请输入修改后的电话：")
        job = input("请输入修改后的职位：")
        addr = input("请输入修改后的地址：")
        card = Card(name, tel, job, addr)
        box.modify_card(card)
    elif code == "4":
        name = input("请输入需要删除谁的名片：")
        box.del_card(name)
    else:
        print("退出系统")
        break
