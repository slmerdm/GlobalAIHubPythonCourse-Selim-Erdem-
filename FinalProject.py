dictionary = {"s1":["Türkiye'nin Başkenti Neresidir?","Ankara"],
            "s2":["Covid-19 Dünyaya Hangi Ülkeden Yayılmıştır?","Çin"],
            "s3":["Cumhuriyet Kaç Yılında Kurulmıştur?", 1923],
            "s4":["İstiklal Marşı Kaç Kıtadır?", 10],
            "s5":["Elon Musk'ın Araç Şirketinin Adı Nedir?","Tesla"],
            "s6":["Telefon Sektöründen En Son Çekilen Firma Hangisidir?","LG"],
            "s7":["Elması ile Ünlü Olan Şehrimiz Neresidir?","Amasya"],
            "s8":["Yetişkin İnsanlarda Kaç Diş Vardır?", 32],
            "s9":["Basketbol Kaç Periyottan Oynanır?", 4],
            "s10":["Bir Futbol Takımı Kaç Kişiden Oluşur?", 11]}

def yarisma():
    puan = 0

    print("SORU-1: ", dictionary["s1"][0])
    cevap1 = input("1. Soru Cevabınız: ")
    if cevap1 == dictionary["s1"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-2: ", dictionary["s2"][0])
    cevap2 = input("2. Soru Cevabınız: ")
    if cevap2 == dictionary["s2"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-3: ", dictionary["s3"][0])
    cevap3 = int(input("3. Soru Cevabınız: "))
    if cevap3 == dictionary["s3"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-4: ", dictionary["s4"][0])
    cevap4 = int(input("4. Soru Cevabınız: "))
    if cevap4 == dictionary["s4"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-5: ", dictionary["s5"][0])
    cevap5 = input("5. Soru Cevabınız: ")
    if cevap5 == dictionary["s5"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-6: ", dictionary["s6"][0])
    cevap6 = input("6. Soru Cevabınız: ")
    if cevap6 == dictionary["s6"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-7: ", dictionary["s7"][0])
    cevap7 = input("7. Soru Cevabınız: ")
    if cevap7 == dictionary["s7"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-8: ", dictionary["s8"][0])
    cevap8 = int(input("8. Soru Cevabınız: "))
    if cevap8 == dictionary["s8"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-9: ", dictionary["s9"][0])
    cevap9 = int(input("9. Soru Cevabınız: "))
    if cevap9 == dictionary["s9"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("SORU-10: ", dictionary["s10"][0])
    cevap1 = int(input("10. Soru Cevabınız: "))
    if cevap1 == dictionary["s10"][1]:
        print("Doğru Cevap")
        puan += 10
    else:
        print("Yanlış Cevap")

    print("Toplam Puanınız:", puan)
    if puan >= 50:
        print("Tebrikler! Kazandınız.")
    else:
        print("Üzgünüz. Kazanamadınız.")
yarisma()
