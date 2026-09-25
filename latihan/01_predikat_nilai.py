nilai = float(input("Masukkan nilai (0-100): "))

if 85 <= nilai <= 100:
    predikat = "A"
elif 70 <= nilai < 85:
    predikat = "B"
elif 65 <= nilai < 70:
    predikat = "C"
elif 50 <= nilai < 65:
    predikat = "D"
elif 0 <= nilai < 50:
    predikat = "E"
else:
    print("Nilai tidak valid")

print(f"Nilai: {nilai} memperoleh predikat: {predikat}")