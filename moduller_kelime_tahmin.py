from random import choice

kelimeler = [
    "fenerbahçe",
    "galatasaray",
    "beşiktaş",
    "trabzonspor",
    "başakşehir",
]

kelime = choice(kelimeler)
bilinen = []

can = 5

while can!=0:
    print("Kalan Hak : {}\n".format(can))
    for harf in kelime:
        if harf in bilinen:
            print(harf, end=" ")
        else:
            print("*",end=" ")


    harf = input("\nHarf Giriniz : ")
    if harf in kelime:
        print("Harf Var")
        bilinen.append(harf)
    else:
        print("Harf Yok")
        can -= 1

    if set(kelime) == set(bilinen):
        print("Tebrikler!")
        break
