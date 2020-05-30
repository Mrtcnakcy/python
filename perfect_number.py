while True:
    sayi=input("Sayı Giriniz: ")
    if(sayi == "q"):
        print("Program Sonlandırılıyor...")
        break
    elif (sayi == ""):
        print("Herhangi Bir Sayı girmediniz Lütfen Bir Sayı giriniz..")
        continue
    else:
        sayi = int(sayi)
        bölen = list()
        for i in range(1, 100000):
            if (sayi % i == 0):
                bölen.append(i)
        bölen.pop()
    print("{} sayısının kendisi hariç bölenleri: {}".format(sayi,bölen))
    print("{} sayısının bölenleri toplamı: {}".format(sayi,sum(bölen)))
    if(sum(bölen)== sayi):
        print("{} bir Mükemmel Sayı ".format(sayi))
    else:
        print("{} bir Mükemmel Sayı Değil :( ".format(sayi))


