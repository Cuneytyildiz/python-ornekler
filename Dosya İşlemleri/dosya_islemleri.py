def harf_notu(satir):

    satir = satir[:-1] # Satır sonlarındaki "\n" yok etmek için son harfi siliyor

    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ortalama = (not1+not2+not3)/3

    if ortalama >= 90:
        harf = "AA"

    elif ortalama >= 85:
        harf = "BA"

    elif ortalama >= 80:
        harf = "BB"

    elif ortalama >= 75:
        harf = "CB"
    elif ortalama >= 70:
        harf = "CC"
    elif ortalama >= 65:
        harf = "DC"
    elif ortalama >= 60:
        harf = "DD"
    elif ortalama >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + "---------------->" + harf + "\n"

def kalanlar(n):
    n = n[:-1]
    liste = n.split("---------------->")
    isim = liste[0]
    harf = liste[1]

    if (harf == "FF") or (harf == "FD"):
        return isim + "---------------->" + "KALDINIZ !!!!" + harf + "\n"


with open("dosya.txt","r",encoding="utf-8") as file:
    kalanlar_listesi = []
    harf_notu_listesi = []
    for i in file:
        harf_notu_listesi.append(harf_notu(i))
        kalanlar_listesi.append(kalanlar(i))


    with open("harf.txt","w",encoding="utf-8") as file2:

        for i in harf_notu_listesi:
            file2.write(i)


        with open("kalanlar.txt","w",encoding="utf-8") as file3:
            for i in kalanlar_listesi:

                file3.write(i)