"""
python中的线程需要使用 threading模块

创建线程的方式一：
  向构造器传递一个可调用对象

1. 需要构造器， 说明有类， 这个类就是 Thread线程类
2. 传递一个可调用对象， 函数默认就是可调用对象
"""
import threading
import time
from threading import Thread


def play_game():
    while True:
        print("正在打游戏", threading.current_thread().name)
        time.sleep(0.5)


# target必须是一个可调用对象， 这个可调用对象是被run()调用的
# 传入的可调用对象其实就是 需要被线程执行的代码
# run()是线程启动后自动调用的， 我们不能手动调用
t = Thread(target=play_game)
# 启动线程
t.start()

for i in range(10):
    print("正在听歌===========================>", i, threading.current_thread().name)
    time.sleep(0.5)
