"""
1. 完成单手数字识别的数量统计
"""
import cv2
import mediapipe as mp

# 加载对应的模块
mp_hand = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# 创建对应的对象
hand = mp_hand.Hands(max_num_hands=1)

# 定义一个列表存储手指指尖的id
hand_tips = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    count = 0
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(frame_rgb)
    mul_hand_landmarks = result.multi_hand_landmarks
    if mul_hand_landmarks is not None:
        for hand_landmarks in mul_hand_landmarks:
            # 绘制手部关键点
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)
            # 获取指尖的坐标
            for tid in hand_tips:
                # tip_x = hand_landmarks.landmark[tid].x
                tip_y = hand_landmarks.landmark[tid].y
                mid_y = hand_landmarks.landmark[tid - 1].y
                if tip_y < mid_y:
                    count += 1
            cv2.putText(frame, f"count: {count}", (100, 100), cv2.FONT_ITALIC,
                        2, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("win", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
