"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak bölenini (EKOK) dönen bir tane fonksiyon yazın.

Örn : 10 12 | 2
       5  6 | 2
       5  3 | 3
       5  1 | 5
       1  1       EKOK(10,12)= 2 * 2 * 3 * 5 = 60

"""
def ekok_alma(sayi1,sayi2):
    i = 2
    ekok = 1
    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i

            sayi1 //= i
            sayi2 //= i


        elif (sayi1 % i == 0 and sayi2 % i != 0):
            ekok *= i

            sayi1 //= i


        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i

            sayi2 //= i
        else:
            i += 1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:",ekok_alma(sayı1, sayı2))