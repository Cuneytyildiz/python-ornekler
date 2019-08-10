"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

"""

def mukemmelsayi(sayi):
    toplam=0
    if sayi>1000 or sayi<1:
        print("Sayı 1 ile 1000 değerleri arasında olmalıdır !!!")
    else:
        for i in range(1,sayi):
            if sayi % i == 0:
                toplam+=i
                if toplam == sayi:
                    print("{}.sayısı mükemmel sayıdır...".format(sayi))
                    return toplam
            else:
                print("Girilen sayı mükemmel sayı değildir !!!")
                return toplam


while True:
    sayi = input("Sayı Giriniz : ")

    if sayi == "q":
        print("Çıkış Yapıldı !!!")
        break

    else:
        sayi = int(sayi)
        mukemmelsayi(sayi)