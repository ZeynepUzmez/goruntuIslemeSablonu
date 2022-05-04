import cv2
import numpy as np
kamera=cv2.VideoCapture(0)#parametre 0 ise pcnin kendi kamerasini acar 1 dersek usb tanimli kamera alir
while True:
    ret,goruntu=kamera.read()
    cv2.rectangle(goruntu, (100,200), (300,500), (0,0,255),2) #♥sytax(goruntu,(solaltx,solalty),(sagustx,sagusty),renkbgr,kalinlik)
    cv2.line(goruntu,(0,0),(100,100),(255,0,0),3)#syntax (goruntu,(baslangicx,baslangicy),(btisx,bitisy),(renkbgr),kalinlik)
    cv2.circle(goruntu,(200,200),40,(0,255,0),3)#syntax (resim,merkeznoktasi kordinat,yaricap,renkbgr,kalinlik)
    cv2.putText(goruntu,"selam",(120,120),cv2.FONT_ITALIC,1,(55,44,3),1)#syntax(goruntu,text,noktaKordinati,fontuTipi,fontbuyuklugu,kalinlik)
    cv2.imshow("kamera goruntusu",goruntu)#kameradan aldigi seyi goruntu icine atar
    if cv2.waitKey(30) & 0xFF == ord('x'): #x e basilmadigi surece 30snde bir goruntu alir 
        break 
kamera.release()
cv2.destroyAllWindows()

