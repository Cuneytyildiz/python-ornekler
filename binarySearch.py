def binarySearch(dizi, aranan, sol, sag):

    while (sol <= sag):

        orta = sol + (sag - sol) // 2

        if dizi[orta] == aranan:
            return orta

        elif dizi[orta] < aranan:
            sol = orta + 1

        elif dizi[orta] > aranan:
            sag = orta - 1

    return -1


dizi = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
aranan = 31

sonuc = binarySearch(dizi, aranan, 0, len(dizi)-1)

if sonuc != -1:
    print("Aradığınız sayı dizinin {}. indeksinde bulunuyor.".format(sonuc))

else:
    print("Aranan değer dizide bulunamadı.")
