# 1'e ve kendisinden başka böleni olmayan sayı = asal sayi

def asal_sayi(n):
    if n == 1:
        return False
    elif n ==2:
        return True
    else:
        for i in range(n):
            if n % 2 == 0 :
                return False
            else:
                return True

sayi = int(input("Asal Sayı Mı Değil Mi : "))
print(asal_sayi(sayi))