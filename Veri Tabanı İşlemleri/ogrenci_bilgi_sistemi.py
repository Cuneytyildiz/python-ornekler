from ogrenci_sinifi import *
import time



print("*"*30)
print('''
1 - Öğrenci Bilgileri
2 - Yeni Öğrenci Kayıtı
3 - Öğrenci Kayıtı Sil
4 - Öğrenci Ara

---> Çıkış Yapmak İçin 'q'
''')

ogrenci = Ogrenciislemleri

while True:
    secim = input("Seçiminiz : ")

    if secim=="q":
        print("Program Sonlandırılıyor...")
        break

    elif (secim=="1"):
        ogrenci.ogrenci_bilgileri()

    elif secim=="2":
        ogrenci_no = input("Öğrenci Numarası : ")
        ogrenci_adi = input("Öğrenci Adı : ")

        yeni_ogrenci = Ogrenci(ogrenci_no,ogrenci_adi)
        print("Öğrenci Ekleniyor...")
        time.sleep(2)

        ogrenci.ogrenci_ekle(yeni_ogrenci)
        print("Başarılı! Öğrenci Eklendi")

    elif secim=="3":
        ogrenci_adi = input("Hangi Öğrenciyi Silmek İstiyorsunuz : ")
        cevap = input("Emin misiniz ? (E/H)")
        if secim=="E":
            print("Öğrenci Siliniyor...")
            time.sleep(2)
            ogrenci.ogrenci_sil(ogrenci_adi)
            print("Başarılı! Öğrenci Silindi")

    elif secim=="4":
        ogrenci_adi = input("Hangi Öğrenciyi Arıyorsunuz : ")
        print("Öğrenci Aranıyor...")
        time.sleep(2)
        ogrenci.ogrenci_sorgulama(ogrenci_adi)

