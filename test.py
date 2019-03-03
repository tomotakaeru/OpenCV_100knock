import cv2

img = cv2.imread("knock100/sample.jpg")
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
