"""
LoGフィルタ
ガウシアンフィルタでノイズ除去したのち，ラプラシアンフィルタでエッジ検出する
画像の端は0パディングする，グレースケール化して扱う
"""
import cv2
import numpy as np

img_original = cv2.imread("sample_noise.jpg")
img = img_original.copy()


#グレースケール化
gray = (0.0722 * img[:,:, 0] + 0.7152 * img[:,:, 1] + 0.2126 * img[:,:, 2]).astype(np.uint8)

h, w = gray.shape
dh = 5
dw = 5
Nh = int(h / dh) + 1
Nw = int(w / dw) + 1

#zero padding
img_ = np.zeros((h + dh - h % dh, w + dw - w % dw))
img_[:h,:w] = gray[:,:]

#ガウシアンフィルタ&ラプラシアンフィルタ
s = 3
#Kernel
K = np.zeros((dh, dw), dtype=np.float)
for x in range(-dw // 2, -dw // 2 + dw):
    for y in range(-dh // 2, -dh // 2 + dh):
        K[y + dh // 2, x + dw // 2] = (x ** 2 + y ** 2 - s ** 2) * np.exp(-(x ** 2 + y ** 2) / (2 * (s ** 2)))
K /= (2 * np.pi * (s ** 6))
K /= K.sum()

for i in range(Nh):
    for j in range(Nw):
        img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] = np.sum(img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] * K)


cv2.imwrite("q19.jpg", img_)
cv2.imshow("ringo", img_)
cv2.waitKey(0)
cv2.destroyAllWindows()
