"""
ガウシアンフィルタ
注目画素の周辺をガウス分布で重みづけ平滑化して，ノイズを除去する
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
            img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1), color] = np.sum(img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1), color] * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16).astype(np.uint8)


cv2.imwrite("q9.jpg", img_)
cv2.imshow("ringo", img_)
cv2.waitKey(0)
cv2.destroyAllWindows()
