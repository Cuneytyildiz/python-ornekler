
def kim(ad,kent,*ozellikler):
    # Ad ve Kent bilgilerini ekrana döker
    print("Adı : ",ad)
    print("Kent : ",kent)

    # Kişisel özellikleri aynı string içinde topla
    ozel=""
    for oz in ozellikler:
        ozel=ozel+" "+oz
    print("Özellikleri : ",ozel)
    print("-"*50)

kim("Hale","Antalya","Esmer","Siyah Saçlı","Ela Gözlü")
kim("Jale","İzmir","Mavi Gözlü")
kim("Vale","İstanbul","Kızıl Saçlı","Yeşil Gözlü")
kim("Lale","Ankara")
