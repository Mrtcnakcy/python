print("*****"
      "Geometrik Şekil Bulma"
      "1-Dörtgen"
      "2-Üçgen"
      "*****")
sekil=input("Bulmak istediğiniz geometrik şeklin adını yazınız: ")

if(sekil == "dörtgen"):
    a=int(input("1.kenar: "))
    b=int(input("2.kenar: "))
    c=int(input("3.kenar: "))
    d=int(input("4.kenar: "))
    if(a == b and a==c and a==d):
        print("Bu bir Kare")
    elif(a==b and c==d):
        print("Bu bir dikdörtgen")
    else:
        print("Bu bir Normal dörtgen")

elif(sekil == "üçgen"):
    a = int(input("1.kenar: "))
    b = int(input("2.kenar: "))
    c = int(input("3.kenar: "))
    if(a==b and a==c):
        print("Bu bir eşkenar üçgendir")
    elif(a==b or a==c or b==c):
        print("Bu bir İkizkenar üçgendir")
    else:
        print("Bu bir normal üçgendir")
else:
    print("Hatalı bir şekil seçtiniz. Lütfen dörtgen veya üçgen şeklinde seçiniz")