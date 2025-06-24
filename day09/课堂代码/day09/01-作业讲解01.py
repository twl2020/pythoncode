"""
1. 使用随机数生成10个随机密码， 密码要求是大小写字母和数字的组合， 长度8位。 提示：使用string模块

分析：
1. 得到大小写字母和数字
2. 需要得到10个8位的密码， 外层循环10次， 内层循环8次即可
3. 8位密码必须是大小写字母和数字的组合
  字母： 随机取出 1-7 个字母
  数字： 8 - 字母的数量
"""

import string
import random


class MyUtils:

    @staticmethod
    def get_password(password_num, count):
        if count < 2:
            return None
        # 存储最终密码的容器
        passwords = []
        # 获取大小写字母和数字
        letter = string.ascii_letters
        digit = string.digits
        for i in range(password_num):
            # choices()： 返回的是列表， 列表中元素的个数就是k的值
            letter_num = random.randint(1, count - 1)
            digit_num = count - letter_num
            letter_password = random.choices(letter, k=letter_num)
            digit_password = random.choices(digit, k=digit_num)
            letter_password.extend(digit_password)
            # shuffle()： 洗牌， 打乱元素的顺序
            random.shuffle(letter_password)
            password = "".join(letter_password)
            passwords.append(password)
        return passwords


if __name__ == '__main__':
    passwords = MyUtils.get_password(10, 1)
    print(passwords)
