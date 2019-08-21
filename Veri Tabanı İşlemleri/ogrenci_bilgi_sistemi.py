import sqlite3
import time

def ogrenciBilgi(ogrenciAdi):
    bilgi = cursor.execute("SELECT * FROM ogrenciler WHERE ogrenci_ad=?",(ogrenciAdi,))
    a = bilgi.fetchall()
    if len(a) == 0 :
        print("Böyle Bir Öğrenci Bulunmamaktadır!")
        time.sleep(3)
        return 0 # Kayıtsız isim girilirse 0 döndürür
    else:
        for i in a:
            print("Öğrenci Numarası :",i[0],"\nÖğrenci Adı : ",i[1])
            print("*** Öğrenci Bilgileri Yükleniyor... ***")
        time.sleep(2)

def dersNotu(ogrenciAdi):
    numara = cursor.execute("SELECT ogrenci_no FROM ogrenciler WHERE ogrenci_ad = ? ",(ogrenciAdi,))
    numara = numara.fetchone()[0] # İlk satırda ne varsa onu döndürür ve dizinin 0. elemanı alır
    notlar = cursor.execute("SELECT * FROM dersNotlari WHERE ogrenci_no = ?",(numara,))
    a = notlar.fetchall()
    print("MATEMATİK : ",a[0][1],"FİZİK : ",a[0][2],"KİMYA : ",a[0][3],"BİYOLOJİ : ",a[0][4])
    time.sleep(3)

def yeniOgrenci(ogrenciAdi):
    cursor.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(ogrenciAdi,))
    print(ogrenciAdi,"isimli öğrenci başarıyla eklenmiştir...")
    time.sleep(3)

def notEkle(ogrenciNo,ders,dersNotu):
    while True:
        bilgi = cursor.execute("SELECT * FROM dersNotlari WHERE ogrenci_no = ?", (ogrenciNo,))
        a = bilgi.fetchall()
        if len(a) == 0:

            if ders == "matematik":

                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,matematik)  VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Matematik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break
            elif ders == "fizik":
                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,fizik) VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Fizik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            elif ders == "kimya":
                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,kimya) VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Kimya Notu Başarıyla Eklendi!")
                time.sleep(3)
                break
            elif ders == "biyoloji":
                cursor.execute("INSERT INTO dersNotlari (ogrenci_no,biyoloji) VALUES (?,?)", (ogrenciNo, dersNotu))
                print("Biyoloji Notu Başarıyla Eklendi!")
                time.sleep(3)
                break
            else:
                print("Hatalı Seçim")
                time.sleep(2)
                break


        else:

            if ders == "matematik":

                cursor.execute("UPDATE dersNotlari SET matematik = ? WHERE ogrenci_no = ?",(dersNotu,ogrenciNo))
                print("Matematik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break



            elif ders == "fizik":

                cursor.execute("UPDATE dersNotlari SET fizik = ? WHERE ogrenci_no = ?", (dersNotu, ogrenciNo))
                print("Fizik Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            elif ders == "kimya":

                cursor.execute("UPDATE dersNotlari SET kimya = ? WHERE ogrenci_no = ?", (dersNotu, ogrenciNo))
                print("Kimya Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            elif ders == "biyoloji":

                cursor.execute("UPDATE dersNotlari SET biyoloji = ? WHERE ogrenci_no = ?", (dersNotu, ogrenciNo))
                print("Biyoloji Notu Başarıyla Eklendi!")
                time.sleep(3)
                break

            else:
                print("Hatalı Seçim")
                time.sleep(2)
                break


def devamsizlikEkle(ogrenciNo,tarih):
    cursor.execute("INSERT INTO devamsizlik VALUES (?,?)",(ogrenciNo,tarih))
    print("Devamsızlık Başarıyla Eklenmiştir!")
    time.sleep(3)

def devamsizlikOgren(ogrenciAdi):
    numara = cursor.execute("SELECT ogrenci_no FROM ogrenciler WHERE ogrenci_ad = ?",(ogrenciAdi,))
    numara = numara.fetchone()[0]

    devamsizlik = cursor.execute("SELECT * FROM devamsizlik WHERE ogrenci_no = ?",(numara,))
    a = devamsizlik.fetchall()
    for i in a :
        print("Gelmediği Tarih : ",i[1])
    time.sleep(3)


print("Öğrenci Bilgi Sistemine Hoşgeldiniz!")
while True:
    baglanti = sqlite3.connect("ogrenciBilgi.db")

    cursor = baglanti.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS 'ogrenciler' ('ogrenci_no' INTEGER ,'ogrenci_ad' TEXT,PRIMARY KEY ('ogrenci_no'))")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS 'dersNotlari' ('ogrenci_no' INTEGER,'matematik' INTEGER,'fizik' INTEGER,'kimya' INTEGER,'biyoloji' INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'devamsizlik' ('ogrenci_no' INTEGER,'devamsizlik_tarih' TEXT)")

    print('''
    1 - Öğrenci Bilgileri
    2 - Yeni Öğrenci Kayıtı
    3 - Ders Notu Ekle
    4 - Devamsızlık Ekle
    q - Çıkış Yap
    ''')

    secim = input("Seçiminiz : ")

    if secim == "1" :
        isim = input("Öğrencinin Adı : ")
        a = ogrenciBilgi(isim)
        if (a != 0): # Fonksiyonda return 0 olup olmadığını kontrol eder

            print('''
               1 - Not Bilgisi
               2 - Devamsızlık Bilgisi
               q - Çıkış
               ''')
            secim = input("Seçiminiz : ")

            while True:
                if secim == "q":
                    break
                elif secim == "1":
                    dersNotu(isim)
                    break
                elif secim == "2":
                    devamsizlikOgren(isim)
                    break
                else:
                    print("Hatalı Tuşlama !!!")


    elif secim == "2":
        isim = input("Eklemek İstediğiniz Öğrencini Adı :")
        yeniOgrenci(isim)
    elif secim == "3":
        numara = input("Öğrenci Numarasını Giriniz : ")
        print("*****DERSLER*****")
        print('''
        matematik
        fizik
        kimya
        biyoloji''')
        secim = input("Ders Seçiniz : ")
        dersNotu = input("Ders Notunu Giriniz : ")
        notEkle(numara,secim,dersNotu)
    elif secim == "4":
        numara = input("Öğrenci Numarasını Giriniz : ")
        tarih = input("Devamsızlık Tarihini Giriniz : ")
        devamsizlikEkle(numara,tarih)
    elif secim == "q":
        print("Çıkış Yapıldı...")
        baglanti.close()
        break
    else:
        print("Hatalı Tuşlama !!!")

    baglanti.commit()
    baglanti.close()