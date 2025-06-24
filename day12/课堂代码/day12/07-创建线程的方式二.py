"""
创建线程的方式二：
    1. 子类继承Thread
    2. 重写run方法

"""
import threading


class MyThread(threading.Thread):
    def run(self):
        # 需要该线程执行的代码就写在这里
        for i in range(10):
            print(self.name, "唱歌", i)


# 创建线程对象
t1 = MyThread(name="子线程01")
t1.start()
