import random

class A:
    alt_limit = 10 # Sınıf Değişkeni
    ust_limit = 99 # Sınıf Değişkeni
    limit_n = 10 # Sınıf Değişkeni

    def __init__(self): self.veriler = []  # Nesne Değişkeni

    def ekle(self,n):
        if len(self.veriler) >= self.limit_n:
            return -1
        if n < self.alt_limit or n > self.ust_limit:
            pass
        else:
            self.veriler.append(n)

def test():
    a = A()
    for n in range(20):
        if a.ekle(random.randint(0,100)) == -1:
            print("Üst limite ulaşıldı: ",a.veriler)
            break
if __name__ == "__main__":
    test()