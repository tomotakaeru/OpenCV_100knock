"""
Embossフィルタ
注目画素の周辺を斜め方向の差分値で埋めて，エッジ検出する
輪郭部分を浮き出しにする
画像の端は0パディングする，グレースケール化して扱う
"""
import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()


# グレースケール化
gray = (0.0722 * img[:,:, 0] + 0.7152 * img[:,:, 1] + 0.2126 * img[:,:, 2]).astype(np.uint8)

h, w = gray.shape
dh = 3
dw = 3
Nh = int(h / dh) + 1
Nw = int(w / dw) + 1

#zero padding
img_ = np.zeros((h + dh - h % dh, w + dw - w % dw))
img_[:h,:w] = gray[:,:]

for i in range(Nh):
    for j in range(Nw):
        img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] = np.sum(img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] * np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])).astype(np.uint8)


cv2.imwrite("q18.jpg", img_)
cv2.imshow("ringo", img_)
cv2.waitKey(0)
cv2.destroyAllWindows()
