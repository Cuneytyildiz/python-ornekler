class Kimlik:
    say = 0
    def __init__(self,ad,meslek):
        self.ad=ad
        self.meslek=meslek
        Kimlik.say+=1
    def meslekDegis(self,meslek):
        self.meslek=meslek

    def __str__(self):
        return self.ad+" : "+self.meslek+" Toplam Üye : "+str(Kimlik.say)

def test():
    k1 = Kimlik("Cüneyt","Öğrenci")
    print(k1)
    k2 = Kimlik("Caner","Avukat")
    print(k2)
    k1.meslekDegis("Mühendis")
    print(k1)

if __name__ == "__main__":
    test()
