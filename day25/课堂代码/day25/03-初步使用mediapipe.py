"""
mediapipe是谷歌提供的一套人工智能解决方案

安装： pip install mediapipe -i https://pypi.tuna.tsinghua.edu.cn/simple/

使用mediapipe的步骤：
1. 导入mediapipe
2. 加载对应功能的模块
3. 创建对应功能的对象
4. 调用处理函数 process


mediapipe实手部关键点和姿态的时候就是以上的步骤，但是代码相对比较繁琐。
使用mediapipe一定一定需要掌握debug, 因为很多的代码要通过调试才能获取。
"""
import mediapipe as mp

# 比如需要完成手部关键点检测， 需要加载对应的功能模块： hands.py
mp_hands = mp.solutions.hands

# 创建对应功能的对象
hand = mp_hands.Hands()

# 调用处理函数 process
hand.process()

