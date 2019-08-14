import random

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    # Tv Kapat
    def tv_kapat(self):
        if self.tv_durum=="Kapalı":
            print("Tv zaten kapalı durumda !!!")
        else:
            print("Televizyon Kapatılıyor...")
            self.tv_durum="Kapalı"

    # Tv Aç
    def tv_ac(self):
        if self.tv_durum=="Açık":
            print("Tv zaten açık durumda !!!")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum="Açık"

    # Tv ses ayarları
    def ses_bilgileri(self):
        while True:
            print("Ses Arttırmak İçin : '+'\nSes Azaltmak İçin : '-'\nMenüye Dönmek İçin : 'q'")
            secim = input("Seçiminiz : ")

            if secim=="+":
                if self.tv_ses!=100:
                    self.tv_ses+=1
                    print("Ses :{}".format(self.tv_ses))
                else:
                    print("Ses daha fazla arttırılmıyor !!!")
            elif secim=="-":
                if self.tv_ses!=0:
                    self.tv_ses-=1
                    print("Ses :{}".format(self.tv_ses))
                else:
                    print("Ses daha fazla azaltılmıyor !!!")
            elif secim=="q":
                print("Ses Güncellendi : {}".format(self.tv_ses))
                break
            else:
                print("Lütfen seçiminizi kontrol ediniz !!!")

    # Menüden kanal ekleme
    def kanal_ekle(self,kanal):
        print("Kanal Eklendi : ",kanal)
        self.kanal_listesi.append(kanal)

    # Rastgele kanal açma
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1) # İndex sayılarını denk getirmek için -1
        self.kanal=self.kanal_listesi[rastgele]

        print("Şu anki Kanal : ",self.kanal)

    def __str__(self):
        return "Tv Durumu : {}\n Ses : {}\nKanallar : {}\n Şu anki Kanal : {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

kumanda = Kumanda()



while True:
    print("*" * 20)
    print("""
    TELEVİZYON UYGULAMASI

    İŞLEMLER :

    1 -> Televizyonu Aç

    2 -> Televiyonu Kapat

    3 -> Televizyon Bilgileri

    4 -> Kanal Sayısı

    5 -> Kanal Ekle

    6 -> Rastgele Kanal'a Geç

    7 -> Ses Ayarları

    Çıkış -> 'q' ya basınız.
    """)
    print("*" * 20)

    işlem = input("Yapmak İstediğiniz İşlem : ")
    if işlem=="q":
        print("Programdan çıkılıyor...")
        break
    elif işlem=="1":
        kumanda.tv_ac()
    elif işlem=="2":
        kumanda.tv_kapat()
    elif işlem=="3":
        print(kumanda)
    elif işlem=="4":
        print("Kanal Sayısı : ",len(kumanda))
    elif işlem=="5":
        kanallar = input("Eklemek istediğiniz kanalları ',' ile ayırarak girin : ")
        eklenecekler = kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal Listesi Başarıyla Güncellendi.")
    elif işlem=="6":
        kumanda.rastgele_kanal()
    elif işlem=="7":
        kumanda.ses_bilgileri()
    else:
        print("Lütfen Seçiminizi Kontrol Ediniz !!!")