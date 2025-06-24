"""
1. 程序启动，提示用户登录或者注册
2. 选择注册->要求输入用户名和密码->将用户名和密码保存到文件 -> 返回注册提示信息
3. 选择登录->要求输入用户和密码->判断是否登录成功

注册: 将用户录入的用户名和密码以下面的格式写入到文件中
用户名1|密码1
用户名2|密码2
"""

import sys


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        """
        根据需求， 保存用户到文件的时候保存的格式是： 用户名1|密码1
        所以我们重写了该方法， 返回用户名|密码
        :return: 用户名|密码
        """
        return f"{self.username}|{self.password}"

    def __eq__(self, other):
        """
        登录的时候我们设计的代码比较的是 对象的内容， 所以需要重写该方法
        """
        if isinstance(other, User):
            return self.username == other.username and self.password == other.password
        return False


class UserManager:

    def register(self, user):
        """
        注册的功能： 就是将user保存到文件中
        :param user: 需要保存的用户
        """
        if not user:
            return False
        try:
            with open("users.txt", mode="at", encoding="UTF-8") as f:
                print(user, file=f, flush=True)
                return True
        except FileNotFoundError as e:
            return False

    def login(self, user):
        with open("users.txt", mode="rt", encoding="UTF-8") as f:
            for line in f:
                username, password = line.strip().split("|")
                db_user = User(username, password)
                # 将user和文件中读取到的用户进行比较
                if user == db_user:
                    return True
            return False


if __name__ == '__main__':
    usermanager = UserManager()
    print("欢迎来到真术学生管理系统".center(30, "*"))
    while True:
        print("1. 注册  2. 登录")
        code = input("请选择:")
        match code:
            case "1":
                username = input("请输入用户名:")
                password = input("请输入密码:")
                b = usermanager.register(User(username, password))
                if b:
                    print("注册成功")
                else:
                    print("注册失败")
            case "2":
                username = input("请输入用户名:")
                password = input("请输入密码:")
                login = usermanager.login(User(username, password))
                if login:
                    print("登录成功")
                    break
                else:
                    print("登录失败")
            case _:
                print("退出系统")
                sys.exit(0)
