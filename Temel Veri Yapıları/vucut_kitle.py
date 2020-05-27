kilo = input("Kilonuzu Giriniz (kg): ")
boy = input("Boyunuzu giriniz (m): ")

bke= round(float(kilo) / (float(boy)**2),2)

print("Benden Kitle Indeksiniz: {}".format(bke))