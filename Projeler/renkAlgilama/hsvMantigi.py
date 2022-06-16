#HSV Hue (Renk Özü),Saturation(Doygunluk)veValue(Parlaklik)dir
#Doygunluk rengin canlılığını belirlerken parlaklık rengin aydınlığını ifade eder.
# HSV de siyah icin renk ve doygunluk değerleri 0 ile 255 arasında herhangi bir sey alabilir iken parlaklık değeri sıfırdır. 
#Beyaz renkte ise ise parlaklık değeri 255'dir.
import cv2
import numpy as np


def nothing(x):
    pass

# Trackbar
cv2.namedWindow("HSVPencere")
cv2.createTrackbar("H", "HSVPencere", 0, 179, nothing)
cv2.createTrackbar("S", "HSVPencere", 255, 255, nothing)
cv2.createTrackbar("V", "HSVPencere", 255, 255, nothing)

img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    h = cv2.getTrackbarPos("H", "HSVPencere")
    s = cv2.getTrackbarPos("S", "HSVPencere")
    v = cv2.getTrackbarPos("V", "HSVPencere")

    img_hsv[:] = (h, s, v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("HSVPencere", img_bgr)
    key = cv2.waitKey(1)
    if key == 27:#esc denk gelir
        break


cv2.destroyAllWindows()