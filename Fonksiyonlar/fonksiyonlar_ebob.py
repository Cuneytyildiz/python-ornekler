"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Örn: 24 32 | 2 *
     12 16 | 2 *
      6  8 | 2 *
      3  4 | 2
      3  2 | 2
      3  1 | 3
      1  1           >> EBOB(24,32) = 2 * 2 * 2 = 8

"""

def ebob_alma(sayi1,sayi2):

    i = 1
    ebob = 1

    while (sayi1 >= i and sayi2>= i):
        if (not (sayi1 % i) and not (sayi2 % i)):
            ebob = i
        i += 1
    return ebob

while True:
    print("EBOB HESAPLAMA")

    sayi1 = input("1.Sayıyı Giriniz : ")
    sayi2 = input("2.Sayıyı Giriniz : ")

    if(sayi1 != "q" and sayi2 != "q"):
        sayi1 = int(sayi1)
        sayi2 = int(sayi2)
        print("Girilen Sayıların EBOB'u :",ebob_alma(sayi1,sayi2))

    else:
        print("Çıkış Yapıldı...")
        break

