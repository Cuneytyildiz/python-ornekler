kullanicilar = []
bakiyeler = {}
giris_yapildi = False
giris_yapan_kullanici = None

def kayit():
    isim = input("Isim: ")
    soyisim = input("Soyisim: ")
    kimlik = input("Kimlik: ")
    eposta = input("E-Posta: ")
    parola = input("Parola: ")

    kullanici = {
        'isim': isim,
        'soyisim': soyisim,
        'kimlik': kimlik,
        'eposta': eposta,
        'parola': parola,
    }

    kullanicilar.append(kullanici)
    bakiyeler[kimlik] = 1000
    return kullanici

def giris():
    kullanici_kimligi = input("Kimlik : ")
    kullanici_parola = input("Parola : ")

    for kullanici in kullanicilar:
        if kullanici['kimlik'] == kullanici_kimligi:
            if kullanici['parola'] == kullanici_parola:
                print("Giriş Yapıldı...")
                print("Güncel Bakiye : ",bakiyeler[kullanici['kimlik']])
                return kullanici
            else:
                print("Parola Hatalı !!!")

    print("Kullanıcı Bulunamadı !!!")
    return None


def para_yatir(kimlik,para):
    bakiyeler[kimlik] += para

def para_cek(kimlik,para):
    if para <= bakiyeler[gonderen]:
        bakiyeler[kimlik] -= para

def transfer(gonderen):
    gonderilen = input("Gönderilecek Kimlik : ")
    miktar = int(input("Miktar : "))
    print(bakiyeler)
    if miktar <= bakiyeler[gonderen]:
        bakiyeler[gonderen] -= miktar
        if gonderilen in bakiyeler:
            bakiyeler[gonderilen] += miktar
    else:
        print("Bakiye Yetersiz !!!")

while True:
    if giris_yapildi:
        print("1. Para Yatir")
        print("2. Para Cek")
        print("3. Transfer")
        print("4. Bakiye Sorgulama")
        print("5. Oturumu Sonlandir")

        secim = int(input("Seciminiz: "))

        if secim == 1:
            para_yatir(giris_yapan_kullanici['kimlik'], 100)
        elif secim == 2:
            pass
        elif secim == 3:
            transfer(giris_yapan_kullanici['kimlik'])
        elif secim == 4:
            print(bakiyeler[giris_yapan_kullanici['kimlik']])
        elif secim == 5:
            giris_yapan_kullanici = None
            giris_yapildi = False
    else:
        print("1. Giris")
        print("2. Kayit")
        print("3. Cikis")

        secim = int(input("Seciminiz: "))

        if secim == 1:
            giris_yapan = giris()
            if giris_yapan is not None:
                giris_yapan_kullanici = giris_yapan
                giris_yapildi = True
        elif secim == 2:
            yeni_kullanici = kayit()
            print(kullanicilar)
            print("Merhaba, {}".format(yeni_kullanici['isim']))
        elif secim == 3:
            break
        else:
            print("\nHatali islem\n")


