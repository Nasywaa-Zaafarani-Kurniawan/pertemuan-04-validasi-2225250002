x = int(input("Masukkan sebuah bilangan bulat: "))

if x > 0:
    if x % 2 == 0:
        print("Bilangan tersebut adalah bilangan positif yang genap.")
    else:
        print("Bilangan tersebut adalah bilangan positif yang ganjil.")
elif x < 0:
    if x % 2 == 0:
        print("Bilangan tersebut adalah bilangan negatif yang genap.")
    else:
        print("Bilangan tersebut adalah bilangan negatif yang ganjil.")
elif x == 0:
    print("Bilangan tersebut adalah nol.")