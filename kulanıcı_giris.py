print("***********"
      "Kullanıcı Giriş"
      "***********")

sys_kullanici_adi = "muratcan"
sys_parola = "159"
giris_hakki=3

while True:
    kullanici_adi = input("Kullanıcı adı: ")
    parola = input("Şifre: ")
    if(kullanici_adi != sys_kullanici_adi and sys_parola == parola):
        print("Kullanıcı Adı Hatalı!")
        giris_hakki -= 1
    elif(kullanici_adi == sys_kullanici_adi and sys_parola!=parola):
        print("Parola Hatalı!")
        giris_hakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
        print("Kullanıcı Adı ve Parola Hatalı!")
        giris_hakki -= 1
    else:
        print("Giriş Başarılı")
        break
    if(giris_hakki==0):
        print("Giriş Hakkınız bitti")
        break