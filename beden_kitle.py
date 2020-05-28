kilo = input("Kilonuzu Giriniz (kg): ")
boy = input("Boyunuzu giriniz (m): ")

bke= round(float(kilo) / (float(boy)**2),2)

if(bke<=18.5):
    print("Zayıf")
elif(bke>18.5 and bke<=25):
    print("Normal")
elif(bke>25 and bke<=30):
    print("Fazla Kilolu")
else:
    print("Obez")
