class Kimlik:
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas
    def __str__(self):
        return self.ad+" - "+ str(self.yas)

class Ogrenci(Kimlik): # Kimlik Sınıfından Miras Alıyor
    def __init__(self,ad,yas,notu):
        Kimlik.__init__(self,ad,yas) # Kimlik sınıfının örneği (instance) oluşturuluyor
        self.notu=notu
    def __str__(self):
        return Kimlik.__str__(self)+" - "+str(self.notu)

def test():
    o1=Ogrenci("Cüneyt", 22 , 90)
    print(o1)

if __name__ == "__main__":
    test()