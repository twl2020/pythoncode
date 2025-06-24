"""
单手数字识别
"""
import cv2
import mediapipe as mp

# 加载对应的模块
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
# 创建对应的对象
hand = mp_hands.Hands(max_num_hands=1)
# 定义一个列表存储手部指尖关键点的序号
hand_tips = [4, 8, 12, 16, 20]
# 记录伸开手指的数量
count = 0
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    # BRG-RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(frame_rgb)
    # 获取所有手的关键点
    mul_hand_landmarks = result.multi_hand_landmarks
    if mul_hand_landmarks is not None:
        # 遍历所有手， 得到每只手的手部关键点
        for hand_landmarks in mul_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # 获取指尖的坐标
            for tip in hand_tips:
                tip_y = hand_landmarks.landmark[tip].y
                mid_y = hand_landmarks.landmark[tip - 1].y
                if tip_y < mid_y:
                    # 手指是伸开的状态
                    count += 1
                else:
                    count -= 1
                # 绘制数量信息
                cv2.putText(frame, f"count: {count}", (100, 100), cv2.FONT_ITALIC,
                            2, (0, 0, 255), 2, cv2.LINE_AA)



    cv2.imshow("frame", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
