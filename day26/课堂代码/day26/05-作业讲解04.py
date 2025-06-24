"""
4. 撑开左手5个手指头分别代表5个不同的小黄人,
并将5个小黄人按序号分别显示在对应的手指头上(直接显示即可不需要去掉背景)
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

# 加载小黄人
# 定义一个列表存储小黄人
xhr_imgs = []
xhr_w, xhr_h = 20, 25

for i in range(1, 6):
    xhr = cv2.resize(cv2.imread(f"resources/xhr_imgs/{i}.png"), (xhr_w, xhr_h))
    xhr_imgs.append(xhr)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    frame_h, frame_w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(frame_rgb)
    mul_hand_landmarks = result.multi_hand_landmarks
    if mul_hand_landmarks is not None:
        for hand_landmarks in mul_hand_landmarks:
            # 绘制手部关键点
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)
            for i, tid in enumerate(hand_tips):
                tip_x = int(hand_landmarks.landmark[tid].x * frame_w)
                tip_y = int(hand_landmarks.landmark[tid].y * frame_h)
                if xhr_h <= tip_y + xhr_h <= frame_h and xhr_w <= tip_x + xhr_w <= frame_w:
                    # 使用切片将小黄人放在每个手指上
                    frame[tip_y:tip_y + xhr_h, tip_x:tip_x + xhr_w] = xhr_imgs[i]

    cv2.imshow("win", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
