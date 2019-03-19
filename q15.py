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
img_v = img_.copy()
img_h = img_.copy()

for i in range(Nh):
    for j in range(Nw):
        img_v[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] = np.sum(img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] * np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])).astype(np.uint8)
        img_h[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] = np.sum(img_[dh * i:dh * (i + 1), dw * j:dw * (j + 1)] * np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])).astype(np.uint8)


cv2.imwrite("q15_v.jpg", img_v)
cv2.imshow("ringo_v", img_v)
cv2.imwrite("q15_h.jpg", img_h)
cv2.imshow("ringo_h", img_h)
cv2.waitKey(0)
cv2.destroyAllWindows()
