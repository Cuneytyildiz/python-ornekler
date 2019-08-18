"""
Problem 3

Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.
"""


with open("mailler.txt","r",encoding="utf-8") as file :
    mailler = file.readlines()
    mail_listesi = list()

    for i in mailler:
        i = i[:-1] # satır sonundaki '\n' silinmesi lazım endswith için
        if (i.endswith(".com") and i.find("@")!=-1):
            mail_listesi.append(i)

    for i in mail_listesi:
        print(i)


