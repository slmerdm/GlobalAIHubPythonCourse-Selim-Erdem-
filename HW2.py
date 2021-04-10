dictionary = {"isim": "selim.1", "sifre": 4321}

a = str(input("Kullanıcı Adı Giriniz: "))
b = int(input("Şifre Giriniz: "))

if dictionary["isim"] == a and dictionary["sifre"] == b:
    print("Tebrikler! Giriş Başarılı")
else:
    print("Kullanıcı Bilgileri Hatalı")
