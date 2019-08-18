class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_icerigi = file.read()

            self.sade_kelimeler = list()
            kelimeler = dosya_icerigi.split()

            for i in kelimeler: # Metin içindeki boşluk ve noktalama işaretleri silinir.
                i = i.strip()
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip("\n")

                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        kelimeler_kumesi = set()

        for i in self.sade_kelimeler: # Boşluk ve noktalama işaretleri silinen kelime listesini, kelimeler kümesine dönüştürür. Kelime tekrarı olmaz.
            kelimeler_kumesi.add(i)

        print("Tüm Kelimeler")

        for i in kelimeler_kumesi:
            print(i)
            print("*"*15)

    def kelime_frekansi(self):
        kelime_sozluk = dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sozluk ): # Listede aynı kelime birden fazla geçiyorsa, o kelimenin adeti 1 arttırılır
                kelime_sozluk[i] += 1

            else:
                kelime_sozluk[i] = 1

        for kelime,sayi in kelime_sozluk.items():

            print("{} kelimesi {} defa geçiyor...".format(kelime,sayi))



metin = Dosya()
metin.kelime_frekansi()