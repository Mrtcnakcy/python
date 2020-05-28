print("***********"
      "Kullanıcı Giriş"
      "***********")

sys_kullanici_adi = "muratcan"
sys_parola = "159"

kullanici_adi = input("Kullanıcı adı: ")
parola = input("Şifre: ")

if(kullanici_adi == sys_kullanici_adi and sys_parola!=parola):
    print("Parola Hatalı!")
elif(kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Kullanıcı Adı Hatalı!")
elif(kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Kullanıcı Adı ve Parola Hatalı!")
else:
    print("Giriş Başarılı.")