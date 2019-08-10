print("""****************
Bir sayının bölenlerini bulma

Programdan çıkmak için 'q' ya basın.
****************
""")


def bolenbul(sayi):
    bolenler = []
    for i in range(2,sayi):
        if sayi % i == 0:
            bolenler.append(i)
    return bolenler

while True:
    deger = int(input("Sayı Giriniz : "))
    if deger == 'q':
        print("Çıkış Yapıldı !!!")
        break
    else:
        print(bolenbul(deger))

