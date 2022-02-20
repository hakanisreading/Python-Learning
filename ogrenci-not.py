yazili1 = float(input("1. yazılı notunuzu giriniz: "))
yazili2 = float(input("2. yazılı notunuzu giriniz: "))
sozlu = float(input("Sözlü notunuzu giriniz: "))

ortalama = (yazili1 + yazili1 + sozlu) / 3

if (ortalama >= 0) and (ortalama < 24):
    print(f"Ortalamanız {ortalama} ve notunuz 0")
elif (ortalama >= 25) and (ortalama < 44):
    print(f"Ortalamanız {ortalama} ve notunuz 1")
elif (ortalama >= 45) and (ortalama < 54):
    print(f"Ortalamanız {ortalama} ve notunuz 2")
elif (ortalama >= 55) and (ortalama < 69):
    print(f"Ortalamanız {ortalama} ve notunuz 3")
elif (ortalama >= 70) and (ortalama < 84):
    print(f"Ortalamanız {ortalama} ve notunuz 4")
elif (ortalama >= 85) and (ortalama <= 100):
    print(f"Ortalamanız {ortalama} ve notunuz 5")
else:
    print("Hatalı bilgi girdiniz. Lütfen tekrar deneyiniz")