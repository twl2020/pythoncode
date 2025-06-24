import cv2

names = ["lee", "zhangsan", "lisi"]
cap = cv2.VideoCapture(0)
face_recognizer = cv2.face.LBPHFaceRecognizer.create()
# 使用人脸识别器对象加到训练好的模型文件
face_recognizer.read("face_recognizer.xml")
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(frame_gray)
    if faces is not None:
        for x, y, w, h in faces:
            face_img = frame_gray[y:y + h, x:x + w]
            # 使用脸部识别区对视频中的图像进行人脸的预测
            # 返回的是预测的标签和置信度
            # opencv中的 置信度越高越不可信
            label, confidence = face_recognizer.predict(face_img)
            if confidence <= 70:
                name = names[label]
            else:
                name = "unknown"

            # 将name绘制在图上
            cv2.putText(frame, name, (100, 100),
                        cv2.FONT_ITALIC, 2,
                        (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("win", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
