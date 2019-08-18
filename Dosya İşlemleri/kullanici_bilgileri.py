"""
ayarlar.txt

---------------
ilkkez=True
lisans=Deneme
serial=321321
kullanıcıadı=
---------------

1 - Kullanıcının daha önce girip girmediğinin bilgisi
2 - Deneme / Full
3 - Serial Numarası
4 - İsim Bilgisi

"""

with open("ayarlar.txt","r+",encoding="utf-8") as file :
    liste = file.readlines()

    # Kullanıcının ilk defa girip girmediğini kontrol eder
    ilkkez = liste[0][:-1] # Satır sonundaki '\n' i siler
    ilkkez_deger = ilkkez.split("=")[1] # splitten sonra oluşan dizideki 1. indeksi seçer

    if(ilkkez_deger == "True"):
        print("Hoşgeldiniz. Sisteme ilk kez giriş yapıyorsunuz!")
        liste[0]="ilkkez=False\n"
        file.seek(0)
        file.writelines(liste)
    else:
        print("Yeniden Hoşgeldiniz!")

# Sürüm kontrolü BAŞLANGIÇ --------------------------------------------------------------->

    lisans = liste[1][:-1]
    lisans_deger=lisans.split("=")[1]

    if (lisans_deger=="Deneme"):

        while True:
            print("\nDeneme Sürümü Kullanıyorsunuz. Son 1 Gün Kaldı !!!")
            print("*" * 20)
            print("Satın Almak İçin : 1\nÇıkış Yapmak İçin :2 ")
            print("*" * 20)

            secim=input("Seçiminiz : ")
            if secim=="1":
                kullanici_anahtar = input("Ürün Anahtarını Giriniz : ")

                anahtar = liste[2][:-1]
                anahtar_deger = anahtar.split("=")[1]

                if kullanici_anahtar == anahtar_deger:
                    # Kayıt Başarılı Bildirimi ------------------->
                    print("\nTEBRİKLER! Full Sürüme Başarı İle Geçtiniz...")
                    liste[1] = "lisans=FULL\n"
                    file.seek(0)
                    file.writelines(liste)
                    #  Kayıt Başarılı Bildirimi <-------------------

                    kullanici_adi = input("Kullanıcı Adınızı Giriniz : ")
                    liste[3] ="kullaniciadi=" + kullanici_adi + "\n"
                    file.seek(0)
                    file.writelines(liste)
                    break
                else:
                    print("\nHATA! Geçersiz Ürün Anahatarı Girdiniz...")

            elif secim=="2":
                print("\nDaha iyi performans için Full sürüme geçmelisiniz !!!")
                break

            else:
                print("\nHatalı Tuşlama !!!")

    else:
        print("Full Sürüm Kullanıyorsunuz. Bütün Avantajlardan Faydalanabilirsiniz!")

#  # Sürüm kontrolü SON  <---------------------------------------------------------------