tarih = 2019

def dogumyilihesapla(yas):
    if yas >= 0:
         yas = tarih - yas
         return yas
    else:
        return print("Yanlış Tarih Belirttiniz !!!")


def yashesapla(dogumyili):
    if dogumyili >= 0:
        dogumyili = tarih - dogumyili
        return dogumyili

    else:
        return print("Yanlış Tarih Belirttiniz !!!")


print("""
***********************
1- Doğum Tarihi Hesapla

2- Yaş Hesapla
***********************
""")

secim = int(input("Seçiminizi Yapınız : "))

if secim == 1:
    a = int(input("Doğum Yılınızı Giriniz :"))
    print(dogumyilihesapla(a))
elif secim == 2:
    b = int(input("Yaşınızı Giriniz : "))
    print(yashesapla(b))