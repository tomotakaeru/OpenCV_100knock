"""
チャネル入れ替え
RGB→BGR
"""
import cv2

img_original = cv2.imread("sample.jpg")
img = img_original.copy()

img[:,:] = img[:,:, (2, 1, 0)]

cv2.imwrite("q1.jpg", img)
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
