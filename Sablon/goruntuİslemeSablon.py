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
#bgr [110 135 115] resim2 icin toplama islemi söyl olur 255 i gecince toplam-225 , gecmezse toplamin kendi olur 
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
cv2.waitKey(0)
cv2.destroyAllWindows()
