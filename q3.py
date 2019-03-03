import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()

h, w, c = img.shape
for i in range(h):
    for j in range(w):
        B = img[i, j, 0]
        G = img[i, j, 1]
        R = img[i, j, 2]
        Y = 0 if (0.2126 * R + 0.7152 * G + 0.0722 * B).astype(np.uint8) < 128 else 255
        img[i, j] = Y

cv2.imwrite("q3.jpg", img)
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
