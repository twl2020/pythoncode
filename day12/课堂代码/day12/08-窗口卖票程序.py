import threading
import time

"""
线程安全问题： 
   多线程的情况下， 可能会出现线程不安全的情况， 线程不安全的表现： 就是数据可能混乱了。

满足以下的条件， 线程一定会出现不安全的情况：
1. 多线程的环境
2. 多线程共享数据
3. 多个线程对共享数据进行修改

满足以上的条件后出现线程不安全的原因是： 一个线程在操作共享数据的时候， 还没有操作完成就被其他线程打乱了。

解决办法： 就是给操作共享数据的代码加锁

加了锁的代码具备原子性
原子性： 不可再分， 也就是说代码是一个整体了， 要么都执行； 要么都不执行。

锁对象threading.Lock：
    实现原始锁对象的类。一旦一个线程获得一个锁，会阻塞随后尝试获得锁的线程，直到它被释放；任何线程都可以释放它。
    锁处于 “锁定” 或者 “非锁定” 两种状态之一，它被创建时为非锁定状态。
    threading.Lock有两个基本方法： acquire() 和 release() 。
    acquire()： 加锁， 获取锁
    release()： 释放锁

"""


# 窗口线程类
class WindowThread(threading.Thread):
    # 票的总数
    ticket_num = 10

    # 创建锁对象
    lock = threading.Lock()

    def run(self):
        # 卖票的代码
        while True:
            # 加锁
            WindowThread.lock.acquire()
            if WindowThread.ticket_num > 0:
                print(f"{self.name}正在卖第{WindowThread.ticket_num}张票")
                WindowThread.ticket_num -= 1
            # 释放锁
            WindowThread.lock.release()
            # 模拟卖票的延迟时间
            time.sleep(0.3)


if __name__ == '__main__':
    # 创建三个窗口线程对象
    t1 = WindowThread(name="窗口1")
    t2 = WindowThread(name="窗口2")
    t3 = WindowThread(name="窗口3")

    # 启动线程
    t1.start()
    t2.start()
    t3.start()
