"""
HSV変換
色相Hを反転
"""
import cv2
import numpy as np

img_original = cv2.imread("sample.jpg")
img = img_original.copy()


def RGBtoHSV(R, G, B):
    Max = max(R, G, B)
    Min = min(R, G, B)
    if Max == Min:
        H = 0
    elif Min == B:
        H = 60 * (G - R) / (Max - Min) + 60
    elif Min == R:
        H = 60 * (B - G) / (Max - Min) + 180
    else:
        H = 60 * (R - B) / (Max - Min) + 300
    S = Max - Min
    V = Max
    return H, S, V

def HSVtoRGB(H, S, V):
    C = S
    H /= 60
    X = C * (1 - np.abs(H % 2 - 1))
    if 0 <= H < 1:
        add = np.array([C, X, 0])
    elif 1 <= H < 2:
        add = np.array([X, C, 0])
    elif 2 <= H < 3:
        add = np.array([0, C, X])
    elif 3 <= H < 4:
        add = np.array([0, X, C])
    elif 4 <= H < 5:
        add = np.array([X, 0, C])
    elif 5 <= H < 6:
        add = np.array([C, 0, X])
    else:
        add = np.array([0, 0, 0])
    RGB = (V - C) * np.array([1, 1, 1]) + add
    return RGB[0], RGB[1], RGB[2]

h, w, c = img.shape
for i in range(h):
    for j in range(w):
        B = img[i, j, 0]
        G = img[i, j, 1]
        R = img[i, j, 2]
        H, S, V = RGBtoHSV(R / 256, G / 256, B / 256)
        R, G, B = HSVtoRGB((H + 180) % 360, S, V)
        img[i, j, 0] = B * 256
        img[i, j, 1] = G * 256
        img[i, j, 2] = R * 256


cv2.imwrite("q5.jpg", img)
cv2.imshow("ringo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
