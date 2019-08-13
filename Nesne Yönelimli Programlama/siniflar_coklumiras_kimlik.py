class Kimlik():
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas
    def __str__(self):
        return self.ad+ " - " + str(self.yas)

class Erisim():
    def __init__(self,tel,eposta):
        self.tel=tel
        self.eposta=eposta
    def ePostaDegis(self,eposta):
        self.eposta = eposta
    def __str__(self):
        return self.tel+" - "+self.eposta
class Ogrenci(Kimlik,Erisim): # Kimlik ve Erisim sınıflarından erisim
    def __init__(self,ad,yas,notu,tel,eposta):
        Kimlik.__init__(self,ad,yas) # Kimlik sınıfı örneği oluşturuluyor
        Erisim.__init__(self,tel,eposta) # Erisim sınıfı örneği oluşturuluyor
        self.notu=notu
    def ePostaDegis(self,eposta): # Overriding (geçersizleştirme) uygulanıyor
        self.eposta="Epostalar İptal Edildi"

    def __str__(self):
        return Kimlik.__str__(self)+" - "+Erisim.__str__(self)+" - "+str(self.notu)

def test():
    o1 = Ogrenci("Cüneyt",22,70,"0555555555","abc@gmail.com")
    print(o1)
    o1.ePostaDegis("abc@gmail.com")
    print(o1)

if __name__ == "__main__":
    test()
