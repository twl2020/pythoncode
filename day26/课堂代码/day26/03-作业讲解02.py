"""
2. 使用姿态掩码图实现人物更换背景的效果
"""
import cv2
import mediapipe as mp
import numpy as np

# 加载姿态模块
mp_pose = mp.solutions.pose

# 创建对象
pose = mp_pose.Pose(enable_segmentation=True)

bg = cv2.imread("resources/gc.jpeg")
person = cv2.imread("resources/ws.jpeg")
person = cv2.resize(person, (750, 500))

person_rgb = cv2.cvtColor(person, cv2.COLOR_BGR2RGB)
# 获取姿态的掩码图
result = pose.process(person_rgb)
# mask掩码图是黑白图像， 颜色范围是： [0.0, 1.0]
# 值越大越接近白色， 也就是我们想要的姿态
mask = result.segmentation_mask
# 将mask变成3通道图像
mask = np.stack((mask, mask, mask), axis=2)
# 去除灰度颜色, 更换背景
result = np.where(mask > 0.7, person, bg)

cv2.imshow("win", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
