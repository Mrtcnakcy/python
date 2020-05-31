print("""**********

ATM Makinesine Hoşgeldiniz

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q' tuşuna basınız.

**********
""")

bakiye = 1000
while True:

    islem=input("İşlemi Seçiniz: ")

    if (islem == "q"):
        print("Yine Bekleriz")
        break

    elif(islem == "1"):
        print("Bakiyeniz {} TL".format(bakiye))

    elif(islem == "2"):
        miktar = int(input("Miktar giriniz: "))
        bakiye += miktar
        print("{} TL Para yatırma işlemi tamamlandı.Yeni bakiyeniz {} TL".format(miktar,bakiye))

    elif(islem == "3"):
        miktar = int(input("Miktar Giriniz: "))
        if(bakiye - miktar < 0):
            print("Hesabınızda {} TL bulunmaktadır. {} TL miktarda para çekemezsiniz".format(bakiye,miktar))
            continue
        bakiye -= miktar
        print("{} TL Para çekme işlemi tamamlandı.Yeni bakiyeniz {} TL".format(miktar,bakiye))

    else:
        print("Geçersiz İşlem")