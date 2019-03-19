"""
減色処理
RGBの各画素値を四値に量子化
"""
import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()


def reduce_color(val):
    if val < 64:
        return 32
    elif val < 128:
        return 96
    elif val < 192:
        return 160
    else:
        return 224

h, w, c = img.shape
for i in range(h):
    for j in range(w):
        B = reduce_color(img[i, j, 0])
        G = reduce_color(img[i, j, 1])
        R = reduce_color(img[i, j, 2])
        img[i, j, 0] = B
        img[i, j, 1] = G
        img[i, j, 2] = R


cv2.imwrite("q6.jpg", img)
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
