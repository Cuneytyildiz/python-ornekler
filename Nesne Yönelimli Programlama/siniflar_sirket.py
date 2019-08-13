class Personel():
    def __init__(self,ad,maas,yetenekler,konum):
        self.ad=ad
        self.maas=maas
        self.yetenekler=yetenekler
        self.konum=konum
        self.gunsayisi=0
        print("Yeni Bir Personel Oluşturuldu. Aramıza Hoşgeldiniz ", self.ad)
    def calis(self):
        print(self.ad,"şu anda çalışıyor. Toplam çalıştığı gün sayısı : ",self.gunsayisi+1)
        self.gunsayisi+=1
    def terfi(self):
        print("Tebrikler !",self.ad,"terfi aldınız. Yeni Maaşınız : ",self.maas+200)
        self.maas+=200
    def bilgilerigoster(self):
        print("*"*15)
        print("Adı : ",self.ad)
        print("Maaşı : ",self.maas)
        print("Yetenekleri : ",self.yetenekler)
        print("Konumu : ",self.konum)
        print("Çalıştığı Gün Sayısı : ",self.gunsayisi)
        print("*" * 15)

class Yonetici(Personel):
    def __init__(self,ad,maas,yetenekler,konum,yonetimbecerisi):
        super().__init__(ad,maas,yetenekler,konum)

        self.yonetimbecerisi=yonetimbecerisi

    def terfi(self):
        print("Tebrikler !", self.ad, "terfi aldınız. Yeni Maaşınız : ", self.maas + 500)
        self.maas += 500

    def calis(self):
        super().calis()
        self.yonetimbecerisi+=0.5
        print("Mevcut Yönetim Becerisi : ",self.yonetimbecerisi)


    def teftis(self):
        print(self.ad,"şu anda teftişe çıktı")

    def bilgilerigoster(self):
        super().bilgilerigoster()
        print("Yönetim Becerisi : ",self.yonetimbecerisi)
        print("*"*15)
caner = Personel("Caner",2000,["İleri Seviye Python"],"Personel")
caner.calis()
caner.calis()
caner.terfi()
caner.bilgilerigoster()

cuneyt = Yonetici("Cüneyt",5000,["Lider"],"Yönetici",80)
cuneyt.teftis()
cuneyt.calis()
cuneyt.terfi()
cuneyt.bilgilerigoster()

