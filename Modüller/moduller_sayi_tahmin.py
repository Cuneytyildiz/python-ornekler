import random

print("""****************************

Sayı Tahmin Oyununa Hoşgeldiniz

1 ile 100 arasında (1 ve 100 dahil) rastgele tahmin edin.
****************************""")
sayi = random.randint(1,100)

can = 5

while can !=0:
    tahmin = int(input("Tahmin : "))

    if sayi > tahmin :
        print("Tahmini Yükselt")
        can -= 1
        print("Kalan Hak : {}".format(can))

    elif sayi < tahmin :
        print("Tahmini Düşür")
        can -= 1
        print("Kalan Hak : {}".format(can))

    else:
        print("Tebrikler Sayıyı Buldunuz ! ")
        break

    if can == 0:
        print("Kaybettiniz !!! ")
        print("Doğru Tahmin {} Olacaktı... ".format(sayi))


