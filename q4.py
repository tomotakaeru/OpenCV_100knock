"""
大津の二値化
分離度Sb^2 / Sw^2 = Sb^2 / (St^2 - Sb^2)が最大，つまりクラス間分散Sb^2が最大となる閾値tを自動決定する
"""
import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()


B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]
Y = (0.2126 * R + 0.7152 * G + 0.0722 * B).astype(np.uint8)

X_max = 0
for t in range(256):
    w0 = np.sum(Y < t) / (np.sum(Y < t) + np.sum(Y >= t))
    w1 = 1 - w0
    M0 = np.mean(Y[Y < t])
    M1 = np.mean(Y[Y >= t])
    X = w0 * w1 * (M0 - M1)** 2
    if X > X_max:
        X_max = X
        th = t
Y[Y < th] = 0
Y[Y >= th] = 255


cv2.imwrite("q4.jpg", Y)
cv2.imshow("ringo", Y)
cv2.waitKey(0)
cv2.destroyAllWindows()
