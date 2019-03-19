"""
モーションフィルタ
注目画素の周辺を対角方向の平均値で埋める
画像の端は0パディングする
"""
import cv2
import numpy as np

img_original = cv2.imread("sample_noise.jpg")
img = img_original.copy()


h, w, c = img.shape
dh = 3
dw = 3
Nh = int(h / dh) + 1
Nw = int(w / dw) + 1

#zero padding
img_ = np.zeros((h + dh - h % dh, w + dw - w % dw, c))
img_[:h,:w] = img[:,:]

for i in range(Nh):
    for j in range(Nw):
        for color in range(c):
            img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1), color] = np.sum(img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1), color] * np.array([[1/3, 0, 0], [0, 1/3, 0], [0, 0, 1/3]])).astype(np.uint8)


cv2.imwrite("q12.jpg", img_)
cv2.imshow("ringo", img_)
cv2.waitKey(0)
cv2.destroyAllWindows()
