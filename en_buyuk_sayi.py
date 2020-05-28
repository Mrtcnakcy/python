print("*****"
      "En Büyük Sayıyı Bulma"
      "*****")

sayi_1= int(input("1.Sayı: "))
sayi_2= int(input("2.Sayı: "))
sayi_3= int(input("3.Sayı: "))

degerler = [sayi_1,sayi_2,sayi_3]
degerler.sort()
print("En büyük sayı: {}".format(degerler[2]))