name = (input("İsminizi giriniz: "))
age = int(input("Yaşınızı giriniz: "))
edu = (input("Eğitim durumunuz: "))

if (age >= 18):
    if (edu == "lise" or edu == "üni"):
        print(f"Ehliyet alabilirsin {name}")
    else:
        print(f"{name} ehliyet alamazsın çünkü eğitim düzeyin yetersiz")
else:
     print(f"{name} ehliyet alamazsın çünkü yaşın uygun değil")

