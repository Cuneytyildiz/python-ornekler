import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *
import sqlite3

baglanti = sqlite3.connect("kutuphane_sistemi.db")
cursor = baglanti.cursor()

yardimFont = QFont("Century Gothic",18)
baslikFont = QFont("Century Gothic",36)
butonFont = QFont("Century Gothic",28)

class intro(QWidget):
    def __init__(self):
        super().__init__()
        yatay = QHBoxLayout()

        self.yazi = QLabel("KÜTÜPHANE SİSTEMİ V1")
        self.yazi.setFont(baslikFont)


        yatay.addStretch()
        yatay.addWidget(self.yazi)
        yatay.addStretch()

        self.setLayout(yatay)
def ustBolum(mevcutpencere):
    kapatButon = QPushButton("X",mevcutpencere)
    kapatButon.setFont(baslikFont)
    kapatButon.setGeometry(1800,20,50,50)
    kapatButon.clicked.connect(Pencere.kapat)

    geriButon = QPushButton("<",mevcutpencere)
    geriButon.setFont(baslikFont)
    geriButon.setGeometry(20,20,50,50)
    geriButon.clicked.connect(mevcutpencere.geriDon)
class Odunclistesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        dikey = QVBoxLayout()
        yatay = QHBoxLayout()

        baslik = QLabel("ÖDÜNÇ İŞLEMLERİ")
        baslik.setFont(baslikFont)

        liste = QListWidget()

        oduncEkle = QPushButton("Ödünç Ver")
        oduncEkle.setFont(butonFont)
        oduncEkle.clicked.connect(self.oduncekle)


        iadeEkle = QPushButton("İade Al")
        iadeEkle.setFont(butonFont)
        iadeEkle.clicked.connect(self.iadeekle)

        oduncler = cursor.execute("SELECT * FROM odunc")
        for i in oduncler.fetchall():
            eklenecek = i[1] +" -----> " + i[2]
            liste.addItem(eklenecek)



        dikey.addWidget(baslik)
        dikey.addWidget(liste)
        dikey.addWidget(oduncEkle)
        dikey.addWidget(iadeEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)

    def ogrenciBilgi(self, item):

        ogrenciismi = item.text()
        kontrol = cursor.execute("SELECT * FROM odunc WHERE ogrenci_adi = ?", (ogrenciismi,))
        say = len(kontrol.fetchall())


        if say == 0:
            QMessageBox.information(self, "ÖĞRENCİ BİLGİSİ", ogrenciismi + " isimli öğrenci kitap almamış !")
        else:
            hangi = cursor.execute("SELECT * FROM odunc WHERE ogrenci_adi = ?", (ogrenciismi,))
            kitap = hangi.fetchall()[0][2]
            QMessageBox.information(self, "ÖĞRENCİ BİLGİSİ",
                                    ogrenciismi + " isimli öğrenicinin elinde şu kitap var :  "+kitap)

    def geriDon(self):
        self.close()
    def oduncekle(self):
        self.yeni = Yeniodunc()
        self.yeni.show()
    def iadeekle(self):
        self.yeni = Yeniiade()
        self.yeni.show()
class Yeniiade(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("İADE AL")

        self.dikey = QVBoxLayout()

        baslik = QLabel("İADE AL")
        baslik.setFont(baslikFont)

        self.ogrenciismi = QLineEdit()
        self.ogrenciismi.setPlaceholderText("Öğrenci Adı")

        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap Adı")

        kaydetButon = QPushButton("Kaydet")
        kaydetButon.clicked.connect(self.kaydet)
        kaydetButon.setFont(butonFont)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogrenciismi)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydetButon)

        self.setLayout(self.dikey)

    def kaydet(self):
        kayit_yazisi = QLabel("Kaydediliyor... Lütfen Bekleyin")
        self.dikey.addWidget(kayit_yazisi)
        QTest.qWait(750)
        ogrenciismi = self.ogrenciismi.text()
        kitapismi = self.kitapismi.text()
        kitapismi2 = kitapismi
        kitapdurumu = "0"
        cursor.execute("DELETE FROM odunc WHERE ogrenci_adi = ? AND kitap_adi = ?",(ogrenciismi,kitapismi))
        cursor.execute("UPDATE kitaplar SET kitap_durum = ? WHERE kitap_adi = ?", (kitapdurumu,kitapismi2))
        baglanti.commit()

        kayit_yazisi.setText("Kayıt Başarılı !")
        QTest.qWait(700)
        self.close()
class Yeniodunc(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ÖDÜNÇ VER")

        self.dikey = QVBoxLayout()

        baslik = QLabel("ÖDÜNÇ VER")
        baslik.setFont(baslikFont)

        self.ogrenciismi = QLineEdit()
        self.ogrenciismi.setPlaceholderText("Öğrenci Adı")

        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap Adı")

        kaydetButon = QPushButton("Kaydet")
        kaydetButon.clicked.connect(self.kaydet)
        kaydetButon.setFont(butonFont)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogrenciismi)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydetButon)

        self.setLayout(self.dikey)

    def kaydet(self):
        kayit_yazisi = QLabel("Kaydediliyor... Lütfen Bekleyin")
        self.dikey.addWidget(kayit_yazisi)
        QTest.qWait(750)
        ogrenciismi = self.ogrenciismi.text()
        kitapismi = self.kitapismi.text()
        kitapismi2 = kitapismi
        kitapdurumu = "1"
        cursor.execute("INSERT INTO odunc (ogrenci_adi,kitap_adi) VALUES (?,?)",(ogrenciismi,kitapismi))
        cursor.execute("UPDATE kitaplar SET kitap_durum = ? WHERE kitap_adi = ?", (kitapdurumu,kitapismi2)) # UPDATE dersNotlari SET fizik = ? WHERE ogrenci_no = ?"
        baglanti.commit()

        kayit_yazisi.setText("Kayıt Başarılı !")
        QTest.qWait(700)
        self.close()
class Ogrencilistesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        dikey = QVBoxLayout()
        yatay = QHBoxLayout()

        baslik = QLabel("ÖĞRENCİ LİSTESİ")
        aciklama = QLabel("Elinde kitap olup olmadığını öğrenmek için öğrencinin üzerine tıklayın !")
        baslik.setFont(baslikFont)

        liste = QListWidget()

        ogrenciEkle = QPushButton("Öğrenci Ekle")
        ogrenciEkle.setFont(butonFont)
        ogrenciEkle.clicked.connect(self.yeniekle)

        ogrenciler = cursor.execute("SELECT * FROM ogrenciler")
        for i in ogrenciler.fetchall():
            liste.addItem(i[1])

        liste.itemClicked.connect(self.ogrenciBilgi)

        dikey.addWidget(baslik)
        dikey.addWidget(aciklama)
        dikey.addWidget(liste)
        dikey.addWidget(ogrenciEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)

    def ogrenciBilgi(self, item):

        ogrenciismi = item.text()
        kontrol = cursor.execute("SELECT * FROM odunc WHERE ogrenci_adi = ?", (ogrenciismi,))
        say = len(kontrol.fetchall())


        if say == 0:
            QMessageBox.information(self, "ÖĞRENCİ BİLGİSİ", ogrenciismi + " isimli öğrenci kitap almamış !")
        else:
            hangi = cursor.execute("SELECT * FROM odunc WHERE ogrenci_adi = ?", (ogrenciismi,))
            kitap = hangi.fetchall()[0][2]
            QMessageBox.information(self, "ÖĞRENCİ BİLGİSİ",
                                    ogrenciismi + " isimli öğrenicinin elinde şu kitap var :  "+kitap)

    def geriDon(self):
        self.close()
    def yeniekle(self):
        self.yeni = Yeniogrenci()
        self.yeni.show()
class Yeniogrenci(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ÖĞRENCİ EKLE")

        self.dikey = QVBoxLayout()

        baslik = QLabel("ÖĞRENCİ EKLE")
        baslik.setFont(baslikFont)

        self.ogrenciismi = QLineEdit()
        self.ogrenciismi.setPlaceholderText("Öğrenci Adı")

        kaydetButon = QPushButton("Kaydet")
        kaydetButon.clicked.connect(self.kaydet)
        kaydetButon.setFont(butonFont)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogrenciismi)
        self.dikey.addWidget(kaydetButon)

        self.setLayout(self.dikey)

    def kaydet(self):
        kayit_yazisi = QLabel("Kaydediliyor... Lütfen Bekleyin")
        self.dikey.addWidget(kayit_yazisi)
        QTest.qWait(750)
        isim = self.ogrenciismi.text()
        cursor.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(isim,))
        baglanti.commit()

        kayit_yazisi.setText("Kayıt Başarılı !")
        QTest.qWait(700)
        self.close()
class Yenikitap(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KİTAP EKLE")

        self.dikey = QVBoxLayout()

        baslik = QLabel("KİTAP EKLE")
        baslik.setFont(baslikFont)

        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap Adı")

        kaydetButon = QPushButton("Kaydet")
        kaydetButon.clicked.connect(self.kaydet)
        kaydetButon.setFont(butonFont)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydetButon)

        self.setLayout(self.dikey)

    def kaydet(self):
        kayıt_yazisi = QLabel("Kaydediliyor... Lütfen Bekleyin")
        self.dikey.addWidget(kayıt_yazisi)
        QTest.qWait(750)
        isim = self.kitapismi.text()
        cursor.execute("INSERT INTO kitaplar (kitap_adi) VALUES (?)",(isim,))
        baglanti.commit()

        kayıt_yazisi.setText("Kayıt Başarılı !")
        QTest.qWait(700)
        self.close()
class Kitaplistesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        dikey = QVBoxLayout()
        yatay = QHBoxLayout()

        baslik = QLabel("KİTAP LİSTESİ")
        aciklama = QLabel("Durumunu Görmek İstediğiniz Kitaba Tıklayınız")
        baslik.setFont(baslikFont)

        liste = QListWidget()

        kitapEkle = QPushButton("Kitap Ekle")
        kitapEkle.setFont(butonFont)
        kitapEkle.clicked.connect(self.yeniekle)

        kitaplar = cursor.execute("SELECT * FROM kitaplar")
        for i in kitaplar.fetchall():
            liste.addItem(i[1])

        liste.itemClicked.connect(self.kitapBilgi)


        dikey.addWidget(baslik)
        dikey.addWidget(aciklama)
        dikey.addWidget(liste)
        dikey.addWidget(kitapEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)

    def kitapBilgi(self,item):

        kitapismi = item.text()
        kontrol = cursor.execute("SELECT * FROM kitaplar WHERE kitap_adi = ?",(kitapismi,))
        durum = kontrol.fetchall()[0][2] # KİTAP DURUMU

        if durum == 0:
            QMessageBox.information(self,"Kitap Durumu",kitapismi+" isimli kitap şu anda boşta !")
        else:
            kimde = cursor.execute("SELECT * FROM odunc WHERE kitap_adi = ?",(kitapismi,))
            ogrenci = kimde.fetchall()[0][1]
            QMessageBox.information(self,"KİTAP DURUMU",kitapismi+" isimli kitap şu anda "+ogrenci+" adlı öğrencide !")

    def yeniekle(self):
        self.yeni = Yenikitap()
        self.yeni.show()
    def geriDon(self):
        self.close()
class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.giris = intro()
        self.giris.showFullScreen()
        QTest.qWait(3000)

        kapatButon = QPushButton("X",self)
        kapatButon.setFont(baslikFont)
        kapatButon.setGeometry(1800, 20, 50, 50)
        kapatButon.clicked.connect(self.kapat)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("KİTAP SİSTEMİ V1")
        baslik.setFont(baslikFont)

        kitapButon = QPushButton("Kitap Listesi")
        kitapButon.setFont(butonFont)
        kitapButon.clicked.connect(self.kitapAc)

        ogrenciButon = QPushButton("Öğrenci Listesi")
        ogrenciButon.setFont(butonFont)
        ogrenciButon.clicked.connect(self.ogrenciAc)

        oduncButon = QPushButton("Ödünç İşlemleri")
        oduncButon.setFont(butonFont)
        oduncButon.clicked.connect(self.oduncAc)

        yardimButon = QPushButton("Hakkımızda / Yardım")
        yardimButon.setFont(butonFont)
        yardimButon.clicked.connect(self.yardimAc)

        dikey.addWidget(baslik)
        dikey.addStretch()
        dikey.addWidget(kitapButon)
        dikey.addStretch()
        dikey.addWidget(ogrenciButon)
        dikey.addStretch()
        dikey.addWidget(oduncButon)
        dikey.addStretch()
        dikey.addWidget(yardimButon)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)
        self.showFullScreen()

    def kitapAc(self):
        self.kitap = Kitaplistesi()
        self.kitap.showFullScreen()

    def kapat(self):
        qApp.quit()

    def ogrenciAc(self):
        self.ogrenci = Ogrencilistesi()
        self.ogrenci.showFullScreen()

    def oduncAc(self):
        self.odunc = Odunclistesi()
        self.odunc.showFullScreen()

    def yardimAc(self):
        self.yardim = Yardimhakkimda()
        self.yardim.showFullScreen()
class Yardimhakkimda(QWidget):
    def __init__(self):
        super().__init__()
        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("YARDIM - HAKKIMIZDA")
        baslik.setFont(baslikFont)

        yazi = QLabel('''
         KÜTÜPHANE SİSTEMİ V1 HAKKINDA
         
            The Zen of Python
                       
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
        ''')
        yazi.setFont(yardimFont)

        dikey.addWidget(baslik)
        dikey.addWidget(yazi)
        dikey.addStretch()

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)
    def geriDon(self):
        self.close()

uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec_())