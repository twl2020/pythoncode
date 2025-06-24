"""
需求： 创建两个子线程， 分别完成 打游戏 和 唱歌
"""
import threading
from threading import Thread
import time


def play_game(num):
    for i in range(num):
        print(threading.current_thread().name + "打游戏", i)
        time.sleep(0.3)


def sing():
    for i in range(10):
        print(threading.current_thread().name + "====》唱歌")
        time.sleep(0.3)


# 创建两个子线程
# t1 = Thread(target=play_game, name="游戏程序的线程", kwargs={"num": 6})
t1 = Thread(target=play_game, name="游戏程序的线程", args=(10,))
t2 = Thread(target=sing, name="歌曲程序的线程")

# 启动线程
t1.start()
t2.start()
