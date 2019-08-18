import sqlite3

class Ogrenci():
    def __init__(self,ogrenci_adi,ogrenci_no):
        self.ogrenci_adi=ogrenci_adi
        self.ogrenci_no=ogrenci_no



    def __str__(self):
        return "Öğrenci Numarası : {}\nÖğrenci Adı : {}".format(self.ogrenci_no,self.ogrenci_adi)




class Ogrenciislemleri():
    def __init__(self):
        self.baglanti_olustur()


    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("ogrenciBilgisi.db")
        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS ogrenciler (ogrenci_no INT,ogrenci_adi TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kapat(self):
        self.baglanti.close()

    def ogrenci_bilgileri(self):
        sorgu = "SELECT * FROM ogrenciler"
        self.cursor.execute(sorgu)

        ogrenciler = self.cursor.fetchall()

        if (len(ogrenciler) == 0):
            print("Kayıtlı Öğrenci Bulunmamaktadır !!!")
        else:
            for i in ogrenciler:
                ogrenci = Ogrenci(i[0],i[1])
                print(ogrenci)
    def ogrenci_ekle(self,ogrenci):
        sorgu = "INSERT INTO ogrenciler VALUES (?,?)"
        self.cursor.execute(sorgu,(ogrenci.ogrenci_adi,ogrenci.ogrenci_no))
        self.baglanti.commit()
    def ogrenci_sil(self,ogrenci):
        sorgu = "DELETE FROM ogreciler WHERE ogrenci_adi = ?"
        self.cursor.execute(sorgu,(ogrenci,))
        self.baglanti.commit()

    def ogrenci_sorgulama(self,ogrenci):
        sorgu = "SELECT * FROM ogrenciler WHERE = ?"
        self.cursor.execute(sorgu,(ogrenci,))

        ogrenciler = self.cursor.fetchall()

        if len(ogrenciler) == 0 :
            print("Böyle bir öğrenci kaydı bulunmamaktadır.")
        else:
            aranan_ogrenci = Ogrenci(ogrenciler[0][0],ogrenciler[0][1])

