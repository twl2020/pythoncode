"""
完成车辆检测案例

分析：
   1. 车辆统计： 在靠近画面下面一个范围的时候才统计， 所以可以截取一个ROI。
   这样做可以减少图像的处理数据和一些干扰
   2. 使用背景减除器得到掩码图像
   3. 使用形态学操作掩码图片
   4. 查找车辆最外层轮廓
   5. 绘制最大外接矩形
   6. 设置一个标准线， 过线的车辆才进行统计
   7. 在视频上绘制车辆数量
"""
import cv2


# 定义一个函数获取矩形框的中心点坐标
def rect_center(x, y, w, h):
    return x + w // 2, y + h // 2


cap = cv2.VideoCapture("resources/car.mp4")
# 创建背景减除器对象
bg_sub = cv2.createBackgroundSubtractorMOG2()
# 创建结构元素
kernel01 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel02 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# offset: 标准线检测车辆过线的一个范围值
offset = 6
# count 记录车辆数量
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 1. 获取图像的roi
    frame_h, frame_w, _ = frame.shape
    frame_roi = frame[frame_h - 400: frame_h, :]
    # 2. 使用背景减除器得到掩码图像
    frame_roi_gray = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2GRAY)
    frame_mask = bg_sub.apply(frame_roi_gray)

    # 3. 使用形态学操作掩码图片
    # 消除白色噪声
    frame_mask = cv2.morphologyEx(frame_mask, cv2.MORPH_OPEN, kernel01, iterations=3)
    frame_mask = cv2.morphologyEx(frame_mask, cv2.MORPH_CLOSE, kernel02, iterations=5)
    frame_mask = cv2.morphologyEx(frame_mask, cv2.MORPH_CLOSE, kernel02, iterations=5)

    # 4. 查找车辆最外层轮廓
    contours, _ = cv2.findContours(frame_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 5. 绘制最大外接矩形
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 70 and h > 70:
            cv2.rectangle(frame_roi, (x, y), (x + w, y + h), (0, 0, 255), 2, cv2.LINE_AA)
            # 得到矩形的中心点坐标
            cx, cy = rect_center(x, y, w, h)
            # 过线的车辆才进行统计
            if frame_h - 200 <= cy + frame_h - 400 <= frame_h - 200 + offset:
                count += 1

        # 在视频上绘制车辆数量
        cv2.putText(frame, f"car counts: {count}", (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2,
                    cv2.LINE_AA)

    # 6. 设置一个标准线， 过线的车辆才进行统计
    cv2.line(frame, (0, frame_h - 200), (frame_w, frame_h - 200), (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("win", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
