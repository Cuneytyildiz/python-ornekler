# 1 - Toplama ||| 2 - Çıkarma ||| 3 - Çarpma ||| 4 - Faktoriyel

import math
import random
import time

skor = 0
while True:

    secim = random.randint(1,4)

    print("Lütfen bekleyin yeni soru hazırlanıyor...")
    time.sleep(2)

    if secim == 1 :
        print("Toplama İşlemi ->")
        sayi1 = random.randint(1,20)
        sayi2 = random.randint(1,20)
        print("{} + {} = ? ".format(sayi1,sayi2))
        sonuc = int(input("Cevap : "))

        if sonuc == sayi1+sayi2:
            print("Tebrikler Doğru Cevap ! ")
            skor+=1
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)
        else:
            print("YANLIŞ !!! Doğru Cevap = ",sayi1+sayi2)
            skor -= 3
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)

    elif secim == 2 :
        print("Çıkarma İşlemi ->")
        sayi1 = random.randint(1,20)
        sayi2 = random.randint(1,20)
        print("{} - {} = ? ".format(sayi1,sayi2))
        sonuc = int(input("Cevap : "))

        if sonuc == sayi1-sayi2:
            print("Tebrikler Doğru Cevap ! ")
            skor += 1
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)
        else:
            print("YANLIŞ !!! Doğru Cevap = ",sayi1-sayi2)
            skor -= 3
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)

    elif secim == 3 :
        print("Çarpma İşlemi ->")
        sayi1 = random.randint(1,10)
        sayi2 = random.randint(1,10)
        print("{} * {} = ? ".format(sayi1, sayi2))
        sonuc = int(input("Cevap : "))

        if sonuc == sayi1 - sayi2:
            print("Tebrikler Doğru Cevap ! ")
            skor += 1
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)
        else:
            print("YANLIŞ !!! Doğru Cevap = ", sayi1*sayi2)
            skor -= 3
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)


    elif secim == 4 :
        print("Faktoriyel İşlemi ->")
        sayi1 = random.randint(1,5)
        print("{}! = ? ".format(sayi1))
        sonuc = int(input("Cevap : "))

        if sonuc==math.factorial(sayi1):
            print("Tebrikler Doğru Cevap ! ")
            skor += 1
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)
        else:
            print("YANLIŞ !!! Doğru Cevap = ", math.factorial(sayi1) )
            skor -= 3
            print("Skorunuz : {} ".format(skor))
            time.sleep(2)
