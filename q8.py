import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()


h, w, c = img.shape
dh = 6
dw = int(1.5 * dh)
Nh = int(h / dh) + 1
Nw = int(w / dw) + 1

for i in range(Nh):
    for j in range(Nw):
        for color in range(c):
            img[dh * i:dh * (i + 1), dw * j:dw * (j + 1), color] = np.amax(img[dh * i:dh * (i + 1), dw * j:dw * (j + 1), color])


cv2.imwrite("q8.jpg", img)
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
