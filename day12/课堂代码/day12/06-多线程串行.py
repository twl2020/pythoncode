"""
串行： 多个线程按照顺序执行

需求： 打游戏结束后才能执行唱歌

join(): 加入线程

线程a.join() 作用： 在哪一个线程中调用 线程a.join(), 哪一个线程就会阻塞， 直到线程a执行完成，才能解除阻塞。
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
t1 = Thread(target=play_game, name="游戏程序的线程", args=(10,))
t2 = Thread(target=sing, name="歌曲程序的线程")

# 启动线程
t1.start()
"""
t1.join()在mainThread中调用的，所以mainThread被阻塞， 直到t1
线程执行完成后， mainThread才能解除阻塞继续执行
"""
# t1.join()
"""
t1.join(1): 在mainThread中调用的， 所以mainThread最多阻塞1s, 到了指定的时间，即使
t1还没有执行完成， mainThread也会解除阻塞继续执行; 
          如果t1线程执行完成后， 指定的阻塞时间还没到， mainThread也会解除阻塞继续执行; 
          
总结：
t1.join(timeout): 什么情况会解除阻塞
1. 时间到了
2. t1执行完了
"""
t1.join(10)
t2.start()