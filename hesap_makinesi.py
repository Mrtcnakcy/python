print("""**********
Hesap Makinesi Programı

İşlemler;

1- Toplama İşlemi
2- Çıkarma İşlemi
3- Çarpma İşlemi
4- Bölme İşlemi
**********
""")

a= int(input("1.Sayı: "))
b= int(input("2.Sayı: "))
islem=input("İşlem Seçiniz: ")

if islem == "1":
    print("{} ile {} toplamı: {}".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} farkı: {}".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} çarpımı: {}".format(a,b,a*b))
elif islem == "4":
    print("{} ile {} bölümü: {}".format(a,b,round(a/b,2)))
else:
    print("Hatalı bir işlem seçtiniz! Lütfen işlemleri 1-2-3-4 yazarak seçiniz.")