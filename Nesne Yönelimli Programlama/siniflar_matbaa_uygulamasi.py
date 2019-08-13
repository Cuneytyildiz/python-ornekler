"""
--> Matbaa makinesi olacak
--> Mürekkebi ve şarjı gibi olaylar olacak
--> Her 20 çalışmada bir dergi ortaya çıkacak
--> Henüz yeni dergi çıkmadıysa yüzde kaçının tamamlandığını gösterecek
--> Yeni dergi çıktığında ona isim verilebilecek

"""
import time

class Makine():
    def __init__(self):
        self.devir = 0 # Çalışma Sayısı
        self.mürekkep = 100 # Mürekkep Oranı
        self.sarj = 100 # Sarj Durumu
        self.dergiler = [] # Eklenecek olan dergi dizisi

    # Makine çalıştığında gerçekleşecek durumlar
    def calis(self):
        if (self.mürekkep >= 6 and self.sarj>=3): # Makinenin çalışması için minimum gereksinimleri karşılaması gerekiyor
            self.devir+=1
            self.mürekkep-=3
            self.sarj-=6
            print("Makine çalışıyor lütfen bekleyiniz...")
            time.sleep(1)

            if self.devir == 20: # Devir sayımız 20 e ulaştığı zaman yenidergi fonksiyonu çağrılır ve devir sıfırlanır
                self.devir = 0
                self.yeniDergi()

        elif(self.mürekkep>= 6 and self.sarj<3):
            print("Yeterli şarj olmadığından devam edilemiyor !!!")
            time.sleep(1)
        elif(self.mürekkep< 6 and self.sarj>=3):
            print("Yeterli mürekkep olmadığından devam edilemiyor !!!")
            time.sleep(1)
        else:
            print("Mürekkep ve sarj az olduğundan devam edilemiyor !!!")
            time.sleep(1)

    # Mürekkep sayımız azalmaya başlayınca doldurma işlemleri
    def murekkepDoldur(self):
        if self.mürekkep<100:
            self.mürekkep+=10
            print("Mürekkep dolduruldu. Mevcut -> ",self.mürekkep)
            time.sleep(0.5)

    # Sarj oranı azalmaya başlayınca doldurma işlemleri
    def sarjDoldur(self):
        if self.sarj<100:
            self.mürekkep+=10
            print("Sarj dolduruldu. Mevcut -> ",self.sarj)
            time.sleep(0.5)

    # 20 devirde oluşacak yeni dergi işlemleri
    def yeniDergi(self):
        print("Yeni dergin çıktı hayırlı olsun")
        isim=input("Yeni Dergiye İsim Giriniz :")
        self.dergiler.append(isim)
        time.sleep(2)

    # Mevcut sistem bilgilerinin görüntülenmesi
    def mevcutDurum(self):
        print("*"*10,"\n Makine Bilgileri\n","*"*10)
        print("Kalan Mürekkep : ",self.mürekkep)
        print("Kalan Sarj : ",self.sarj)
        print("Toplam Çıkarılan Dergi Sayısı : ",len(self.dergiler))
        if (len(self.dergiler)>0):
            for adet in self.dergiler:
                print(adet)
        print("Yeni çıkacak olan derginin %",self.devir*5,"kısmı tamamlandı...") # 20 devirde 1 dergi çıktığı için yüzdelik kısmı bulmak için 5 ile çarpıyoruz
        print("*"*10)
        time.sleep(2)

makine1 = Makine() # Makinemizin adı

while True:
    print("-"*30)
    print("""
    1 -> Makineyi Çalıştır
    2 -> Mevcut Durumu Bilgileri
    3 -> Mürekkep Doldur
    4 -> Sarj Doldur
    5 -> Çıkış 
    """)
    print("-"*30)

    komut = input("Seçiminiz : ")

    if komut == "1" :
        makine1.calis()

    elif komut == "2" :
        makine1.mevcutDurum()

    elif komut == "3" :
        makine1.murekkepDoldur()

    elif komut == "4" :
        makine1.sarjDoldur()

    elif komut == "5" :
        print("Çıkış Yapıldı")
        break

    else:
        print("Hatalı Tuşlama !!!")


