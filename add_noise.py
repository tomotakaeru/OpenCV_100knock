import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()


h, w, c = img.shape
s_vs_p = 0.5
amount = 0.005

num_salt = np.ceil(amount * img.size * s_vs_p)
coords = [np.random.randint(0, i-1 , int(num_salt)) for i in img.shape]
img[coords[:-1]] = (255, 255, 255)

num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
coords = [np.random.randint(0, i-1 , int(num_pepper)) for i in img.shape]
img[coords[:-1]] = (0, 0, 0)


cv2.imwrite("sample_noise.jpg", img)
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
