"""
姿态关键点
"""
import cv2
import mediapipe as mp

# 加载对应的模块
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
# 创建对应的对象
pose = mp_pose.Pose()

img = cv2.imread("resources/ws.jpeg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
"""
pose对象的处理函数返回NamedTuple有三个字段：
1. pose_landmarks 姿态的关键点
2. pose_world_landmarks 姿态的3D关键点
3. segmentation_mask  分离出来的姿态掩码， 要求参数enable_segmentation=True
"""
result = pose.process(img_rgb)
# 绘制关键点
pose_landmarks = result.pose_landmarks
# mp_draw.draw_landmarks(img, pose_landmarks, mp_pose.POSE_CONNECTIONS)

# 绘制姿态3D坐标的关键点
mp_draw.plot_landmarks(pose_landmarks, mp_pose.POSE_CONNECTIONS)
cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()