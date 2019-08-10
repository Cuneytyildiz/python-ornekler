# n sayısı çiftse n = n // 2, n sayısı tekse n = 3 * n + 1 olsun ve fonksiyon kendi kendini n==1 olana kadar tekrarlasın

def collatz_dizisi(sayi):
    if sayi%2==0:
        print(sayi//2)
        return sayi//2
    else:
        sonuc = (3*sayi)+1
        print(sonuc)
        return sonuc

n = input("Bir Değer Giriniz : ")

while n!=1:
    n = collatz_dizisi(int(n))