import cv2
import numpy as np

data = False

x0, y0 = -1, -1
drawing = False


def mouse(event, x, y, flags, params):
    global x0, y0, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x0, y0 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(bg, (x0, y0), (x, y), (0, 0, 255), 3, cv2.LINE_AA)
            x0, y0 = x, y
            cv2.imshow('win', bg)


bg = np.zeros((480, 640, 3), 'u1')
cv2.namedWindow('win', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('win', mouse)
cv2.imshow('win', bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
