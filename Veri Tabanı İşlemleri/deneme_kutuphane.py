import sqlite3

con = sqlite3.connect("denemekutuphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def kullanici_veri(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()
    print("****** Kitap Bilgileri ******* ")
    for i in liste:
        print(i)

def kitap_yazar_bilgileri():
    cursor.execute("SELECT İsim,Yazar FROM kitaplık")
    liste = cursor.fetchall()
    print("****** Kitap - Yazar  Bilgileri ******* ")
    for i in liste:
        print(i)
def yayinevi_sorgulama(yayinevi):
    cursor.execute("SELECT * FROM kitaplık WHERE Yayınevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("****** Yayınevi Bilgileri ******* ")
    for i in liste:
        print(i)

def yayinevi_guncelle(eski,yeni):
    cursor.execute("UPDATE kitaplık SET Yayınevi = ? WHERE Yayınevi = ?",(yeni,eski))
    con.commit()

def kitap_sil(kitap):
    cursor.execute("DELETE FROM kitaplık WHERE İsim = ?",(kitap,))
    con.commit()

verileri_al()
kitap_sil("İstanbul Hatırası")
verileri_al()


""" # Yayınevi Güncelleme
verileri_al()
yayinevi_guncelle("Everest","Yeni Yayınevi")
verileri_al()
"""




#tablo_olustur()
#veri_ekle()

#verileri_al()
#kitap_yazar_bilgileri()
#yayinevi_sorgulama("Destek Yayınları")


"""# Kitap ekleme
print("*"*10)
isim = input("Kitap İsmi : ")
yazar = input("Yazar : ")
yayinevi = input("Yayınevi : ")
sayfa_sayisi = input("Sayfa Sayısı :")
print("*"*10)
kullanici_veri(isim,yazar,yayinevi,sayfa_sayisi)
"""




con.close()