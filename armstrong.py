sayi=input("Sayi: ")
basamak = len(sayi)
liste=list()

if(basamak == 1):
    for i in sayi:
        islem = int(i) ** 1
        liste.append(islem)
elif(basamak == 2):
    for i in sayi:
        islem = int(i) ** 2
        liste.append(islem)
elif(basamak == 3):
    for i in sayi:
        islem = int(i) ** 3
        liste.append(islem)
elif(basamak == 4):
    for i in sayi:
        islem = int(i) ** 4
        liste.append(islem)

if (sum(liste) == int(sayi)):
    print("Bu bir Armstrong sayısıdır")
else:
    print("Bu bir Armstrong sayısı değildir")



