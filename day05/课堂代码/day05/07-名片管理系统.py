"""
名片管理 系统 录入三张名片即可
名片盒子 列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?

cards = [
{“name”:”张三”,”tel”:”13812345678”,”job”:”CEO”,”addr”:”四川”}, # 字典
{名片信息2},
{名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字
典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""


# 添加名片
def add_card():
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    job = input("请输入职位：")
    addr = input("请输入地址：")
    card = {"name": name, "tel": tel, "job": job, "addr": addr}
    cards.append(card)


def show_card():
    for card in cards:
        print(card)


def modify_card():
    name = input("请输入需要修改谁的名片：")
    # 判断名片盒子中是否存在该用户的名片
    for card in cards:
        # 说明存在该用户的名片
        if card["name"] == name:
            card["name"] = input("请输入修改后的名字：") or card["name"]
            card["tel"] = input("请输入修改后的电话：") or card["tel"]
            card["job"] = input("请输入修改后的职位：") or card["job"]
            card["addr"] = input("请输入修改后的地址：") or card["addr"]


def del_card():
    name = input("请输入需要删除谁的名片：")
    for card in cards:
        # 说明存在该用户的名片
        if card["name"] == name:
            cards.remove(card)


# 存储名片信息的盒子
cards = []
print("欢迎进入真术名片管理系统".center(30, "*"))
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
