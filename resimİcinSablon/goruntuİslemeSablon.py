import cv2
import numpy as np
resim=cv2.imread("papatya.jpg")
resim2=cv2.imread("gul.jpg")
#resim=cv2.imread("papatya.jpg",0) resmi siyah beyaz acma
#cv2.imshow("papatya",resim)
##################
#resmin reklerinin matrix karsiligi/boyutu/datatype bulma
#print(resim[(230,80)]) resmin dikine 230enine 80 parçasının rengi bgr
#print(resim) resmin renklerinin matrix karşiligi
#cv2.imwrite("siyahBeyazLogo.png",resim) resmin siyah beyaz halini olusturma
#print(resim.size) resmin boyutunu bulma
#print(resim.dtype) resimn data type bulma
#print(resim.shape)
##################
#kesit alma
#for i in range(100):
    #resim[70,i]=[255,255,255]
#cv2.imshow("papatya",resim)   
###################
#resimde kesit alma efekt uygulama
#resim[:,:,1]=255#bgr old icin resim[:,:,0]-255=mavi efekt ,resim[:,:,1]-255 yesil  efekt resim[:,:,2]-255kırmzı efekt
#resim[100:250,200:400,0]=240# burada yde 100/250 arası ve xde 200/400 arasi mavi efekt uyguladik
#cv2.imshow("papatya efektli",resim)
##################
#resimi  aynalama ,uzatma,tekrarlama,cerceve ekleme
#kesit=resim[50:250,0:200]#resim yde 50/250 arasi xde 0/200 arasi
#resim[50:250,0:200]=kesit
#resim[50:250,0:200]=(0,150,100) #resimin belli kısmına (b,g,r) verme
#cv2.imshow("kesit resim",kesit)
#aynalama=cv2.copyMakeBorder(resim, 250, 250, 250, 250, cv2.BORDER_REFLECT)
#resimuzatma=cv2.copyMakeBorder(resim, 150, 150, 150, 150, cv2.BORDER_REPLICATE)
#resimtekrar=cv2.copyMakeBorder(resim, 500, 500, 500, 500, cv2.BORDER_WRAP)
#resimcerceve=cv2.copyMakeBorder(resim, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=(75,150,255))
#cv2.imshow("aynali resim",aynalama)
#cv2.imshow("uzatmali resim",resimuzatma)
#cv2.imshow("tekrarli resim",resimtekrar)
#cv2.imshow("cerceveli resim",resimcerceve)
###############################################
#resimde bölgeyi ilk önce sol alt köşenin x-y sini sonra sağ üst köşenin x-y sini vererek dikdörtgen içine alma
# syntax (sol alt (x,y), sağ üst(x,y),renkkodu, kalınlık)
#cv2.rectangle(resim,(255,220),(320,120),[0,0,255],3)
#cv2.imshow("dikdortgenli resim",resim)
#################################################
#resimleri ust uste ekleme
#resimler ayni boytta olmali degilse düzenlemelisin yoksa hata alirsin
#toplam=cv2.add(resim,resim2)#resimleri topladik
#cv2.imshow("ust uste resim", toplam)
#agirlikli toplama
#parametreler ilk resim ,agirlik1,ikinci resim,agirlik2,0
#toplam2=cv2.addWeighted(resim, 0.3, resim2 ,0.7, 0)
#cv2.imshow("ust uste resim2", toplam2)
##############################################
#agirlikli toplam
#bgr [3 51 39] resim icin
#bgr [110 135 115] resim2 icin toplama islemi söyle olur 255 i gecince toplam-256 , gecmezse toplamin kendi olur 
#bgr toplam sonucu [113 186 154] olur
#print(resim[10,50])
#print(resim2[10,30])
#print(resim[10,50]+resim2[10,30])
###################################
#resim grilestirme
#resimgri=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gri resim",resimgri)
#yukseklik,genislik,kanalS=resim.shape
#yukseklikG,genislikG=resimgri.shape#gri resmin kanal s yok 
#print("ilk",yukseklik,genislik,kanalS)
#print("gri",yukseklikG,genislikG)
###
#grilesme 2. yol
#resimgri2=cv2.imread("papatya.jpg",0)
#cv2.imshow("ikincigri",resimgri2)
########################################
#goruntu piramitleri 
#goruntuyu buyutup kucultme
#ikiKatBuyuk=cv2.pyrUp(resim2)#genisligi ve yuksekligi iki kat arttirir
#ikiKatKucuk=cv2.pyrDown(resim2)#genisligi ve yuksekligi iki kat azaltir
#cv2.imshow("orijinal",resim2)
#cv2.imshow("buyuk",ikiKatBuyuk)
#cv2.imshow("kucuk",ikiKatKucuk)
#print("orijinal resim boyut:",resim2.shape)
#print("iki kat resim boyut:",ikiKatBuyuk.shape)
#print("iki kat resim boyut:",ikiKatKucuk.shape)
## resim olusturma ve ekrana matrixini yazdirma
#zeros elemanlari sifirdan olusan matrix olusturur
#resimOlustur=np.zeros((300,300,3),dtype="uint8") syntaxı((resminGenisligi,resminYuksekligi,kanalSayisi),dtype)
#print(resimOlustur)
#########################
#cizgi-daire-metinKutusu olusturma
#resimOlustur=np.zeros((300,300,3),dtype="uint8") #syntaxı((resminGenisligi,resminYuksekligi,kanalSayisi),dtype)
#cv2.line(resimOlustur,(0,0),(100,100),(0,0,255),3)# kirmizi 3 kalinliginda cizgi cizme 0,0 dan 100,100 noktasina kadar
#cv2.circle(resimOlustur,(150,150),25,(0,255,0),4)#cember cizme
#cv2.putText(resimOlustur,"Merhabalar",(110,110),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)#yazi ekleme
#cv2.imshow("yeni Hali",resimOlustur)
########################
#filtreleme
#mean dogrusal filtredir
#gausian ve median lineer degildir 
gurultulu=cv2.imread("gurultuluResim.jpg")
#cv2.imshow("orijinal resim",gurultulu)
#meanİyilestirilmis=cv2.blur(gurultulu,(3,3))#gurultulu resmi 3*3luk matrixlerin ort alarak  bulaniklastirarak yumusatir
#cv2.imshow("mean1 resim",meanİyilestirilmis)
#meanİyilestirilmis2=cv2.blur(gurultulu,(4,4))#gurultulu resmi 4*4luk matrixlerin ort alarak bulaniklastirarak yumusatir 
#cv2.imshow("mean2 resim",meanİyilestirilmis2)
#medianİyilestirilmis=cv2.medianBlur(gurultulu, 3)#gurultulu resmi 3*3 luk matrix icindeki degerlerin medianını alarak bulaniklastirarak yumusatir
#cv2.imshow("median resim2",medianİyilestirilmis)
#medianİyilestirilmis2=cv2.medianBlur(gurultulu, 5)#gurultulu resmi 5*5 luk matrix icindeki degerlerin medianını alarak bulaniklastirarak yumusatir
#cv2.imshow("median resim2",medianİyilestirilmis2)
#gausianİyilestirilmis=cv2.GaussianBlur(gurultulu, (3,3), 0)# gaus denklemi ile 3*3 matrix icindeki degerleri bulaniklastirararak yumusatir
#cv2.imshow("gausian resim1",gausianİyilestirilmis)
#gausianİyilestirilmis=cv2.GaussianBlur(gurultulu, (5,5), 0)# gaus denklemi ile 5*5 matrix icindeki degerleri bulaniklastirararak yumusatir
#cv2.imshow("gausian resim2",gausianİyilestirilmis)
############################
#morfolojik islemler
#bu islemler siyah beyaz resimlerde daha basarili old icin  resmin siyah beyaz   halini kullandik
resimSiyahB=cv2.imread("papatya.jpg",0)
kernel=np.ones((5,5),np.uint8)
#dilation=cv2.dilate(resimSiyahB,kernel,iterations=1)#beyazlari genisletme amaci tasir iterations u arttirirsak goruntude beyazlar artar
#cv2.imshow("original",resimSiyahB)
#cv2.imshow("dilate",dilation)
#erosion=cv2.erode(resimSiyahB, kernel,iterations=1)# beyazlara asindirma islemi yapar
#cv2.imshow("erosion",erosion)
#erosion kullandigin resimin ustune dilaiton kullanıp gurultu giderme yapabilirsin
#opening=cv2.morphologyEx(resimSiyahB, cv2.MORPH_OPEN, kernel)#erosion ustune dilasion yapar
#cv2.imshow("opening resim",opening)
#closing=cv2.morphologyEx(resimSiyahB, cv2.MORPH_CLOSE, kernel)#dilasion ustune erosion yapar
#cv2.imshow("closing resim",closing)
#morfGrad=cv2.morphologyEx(resimSiyahB, cv2.MORPH_GRADIENT, kernel)#dilaiton-erosion 
#tophat=cv2.morphologyEx(resimSiyahB, cv2.MORPH_TOPHAT, kernel)#orijinalResim-opening
#cv2.imshow("tophat resim",tophat)
#blackhat=cv2.morphologyEx(resimSiyahB, cv2.MORPH_BLACKHAT, kernel)#closing - orijinalResim
#cv2.imshow("black resim",tophat)
#################################
#esik deger 
#daha iyi sonuc almak icinrenkli bir resim kullandik
#simple thresholdlar
kus=cv2.imread("kus.png")
#cv2.imshow("orijinal", kus)
#ret,threshold=cv2.threshold(kus,125,255,cv2.THRESH_BINARY)#min value yani 125 altindakiler sıfıra yuvarlanir
#cv2.imshow("treshold resim1",threshold)
#ret,threshold2=cv2.threshold(kus,125,255,cv2.THRESH_BINARY_INV)#min value yani 125 altindakiler sıfıra yuvarlanir
#cv2.imshow("treshold resim2",threshold2)
#ret,threshold3=cv2.threshold(kus,125,255,cv2.THRESH_TRUNC)#min value yani 125 altindakiler sıfıra yuvarlanir
#cv2.imshow("treshold resim3",threshold3)
#ret,threshold4=cv2.threshold(kus,125,255,cv2.THRESH_TOZERO)#min value yani 125 altindakiler sıfıra yuvarlanir
#cv2.imshow("treshold resim4",threshold4)
#ret,threshold5=cv2.threshold(kus,125,255,cv2.THRESH_TOZERO_INV)#min value yani 125 altindakiler sıfıra yuvarlanir
#cv2.imshow("treshold resim5",threshold5)
#adaptive thresholding
#th2 = cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
 #           cv2.THRESH_BINARY,10,7)
#cv2.imshow("Athresh",th2)
#th3 = cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 #           cv2.THRESH_BINARY,11,2)
#cv2.imshow("Athresh",th3)
#otsu thresholding
#ret,Othres=cv2.threshold(kus,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#cv2.imshow("otsu thresh",Othres)
#####################
#canny kenar algilama
#gri resimlerde blurlama yapacaz
#gray=cv2.cvtColor(kus,cv2.COLOR_BGR2GRAY)
#blur=cv2.GaussianBlur(gray,(3,3) , 0)
#cv2.imshow("blurlu kus",blur)
#canny=cv2.Canny(blur,50,150)#syntax (resim,altesik,ustesik)
#cv2.imshow("canny resim",canny)
#otomatik canny
#def autoCanny(blur,sigma=0.44):
    #median=np.median(blur)
    #altEsik=int(max(0,1.0-sigma*median))
    #ustEsik=int(min(255,1.0+sigma*median))
    #canny=cv2.Canny(blur,altEsik,ustEsik)
    #return canny

#genisKenarAlg=cv2.Canny(blur,10,220)
#darKenarAlg=cv2.Canny(blur,200,230)
#auto=autoCanny(blur)
#cv2.imshow("kenarlar",np.hstack([genisKenarAlg,darKenarAlg,auto]))#tum resimleri sirali getirdik
#bitwise operatorleri(and ,or ,not,xor)
resimSiyahB2=cv2.imread("gul.jpg",0)
#andBws=cv2.bitwise_and(resimSiyahB, resimSiyahB2)
#cv2.imshow("bitwise and",andBws)
#orBws=cv2.bitwise_or(resimSiyahB, resimSiyahB2)
#cv2.imshow("bitwise or",orBws)
#xorBws=cv2.bitwise_xor(resimSiyahB, resimSiyahB2)
#cv2.imshow("bitwise xor",xorBws)
#notBws1=cv2.bitwise_not(resimSiyahB)
#cv2.imshow("bitwise not",notBws1)
#notBws2=cv2.bitwise_not(resimSiyahB2)
#cv2.imshow("bitwise not2",notBws2)


    
cv2.waitKey(0)
cv2.destroyAllWindows()
