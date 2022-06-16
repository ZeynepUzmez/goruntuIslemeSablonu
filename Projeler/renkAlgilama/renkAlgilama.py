import cv2

kamera = cv2.VideoCapture(0)  
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, goruntu = kamera.read()
    hsv_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)#bgr hsv cevirdik
    height, width, ret = goruntu.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_goruntu[cy, cx]
    hue_value = pixel_center[0]
#burada s ve ve nin 255 old dusunerek tasarladik
    color = "Undefined"
    if hue_value < 5:
        color = "KIRMIZI"
    elif hue_value < 22:
        color = "Turuncu"
    elif hue_value < 33:
        color = "SARI"
    elif hue_value < 78:
        color = "YEŞİL"
    elif hue_value < 131:
        color = "MAVi"
    elif hue_value < 170:
        color = "MOR"
    else:
        color = "KIRMIZI"

    pixel_center_bgr = goruntu[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(goruntu, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(goruntu, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(goruntu, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Goruntu", goruntu)
    key = cv2.waitKey(1)
    if key == 27:#esc denk gelir
        break

kamera.release()
cv2.destroyAllWindows()