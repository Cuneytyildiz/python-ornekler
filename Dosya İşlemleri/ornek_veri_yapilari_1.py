"""Problem 1

Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.

İpucu : Kodlama egzersizimizde buna çok benzer bir şey yapmıştık.
"""


kelime = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

kelime_sozluk = dict()

for i in kelime:
    if ( i in kelime_sozluk):
        kelime_sozluk[i] += 1
    else:
        kelime_sozluk[i] = 1

for kelime,sayi in kelime_sozluk.items():
    print("*"*10)
    print("{} harfi {} defa geçiyor...".format(kelime,sayi))



