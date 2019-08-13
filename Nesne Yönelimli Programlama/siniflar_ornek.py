class Sayiİslem:
    def __init__(self):
        self.sayi = 0
    def onEkle(self,kac):
        self.__sayi = kac
        return self.__sayi+10
    def besleCarp(self,kac):
        self.__sayi = kac
        return self.__sayi*5

sayi = Sayiİslem()
print(sayi.onEkle(7))
print(sayi.besleCarp(12))
