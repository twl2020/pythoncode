"""
手部关键点检测：
1. 使用opencv捕获摄像头
2. 使用mediapipe进行手部关键点识别
"""
import cv2
import mediapipe as mp

# 加载对应功能的模块
mp_hand = mp.solutions.hands
# 加载绘制功能的模块
mp_draw = mp.solutions.drawing_utils
# 创建对应功能的对象
hand = mp_hand.Hands()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 视频中的画面是镜像后的， 所以视频中的图像需要翻转
    # flipCode == 0   垂直翻转
    # flipCode > 0   水平翻转
    # flipCode < 0   水平垂直翻转
    frame = cv2.flip(frame, 1)

    # BRG-RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 手部关键点检查
    # 以下的函数返回的是 NamedTuple， 里面包含三个属性：
    # multi_hand_landmarks： 检测到的所有手的关键点
    # multi_hand_world_landmarks： 检测到的所有手的关键点， 3D
    # multi_handedness： 检测到的手的信息（包含了手的类型）
    result = hand.process(frame_rgb)
    # 获取手部关键点
    mul_hand_landmarks = result.multi_hand_landmarks
    if mul_hand_landmarks is not None:
        # hand_landmarks里面的landmark存储的是手部21个关键点坐标
        # 关键点坐标的xyz值是一个比例值
        for hand_landmarks in mul_hand_landmarks:
            # 将手部关键点绘制出来
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

    cv2.imshow("frame", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
