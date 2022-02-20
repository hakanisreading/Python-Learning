name = str(input("İsminizi giriniz: "))
age = int(input("Yaşınızı giriniz: "))
edu = str(input("Eğitim durumunuz: "))

if age >= 18:
    print(f"Ehliyet almak için yaşın uygun {name}")
    if edu == "lise" or "üni":
        print(f"Ehliyet almak için eğitim durumun uygun {name}")
else:
    print(f"{name} ehliyet alamazsın çünkü yaşın ya da eğitim düzeyin uygun değil. En az 18 yaşında ve lise mezunu olmalısın")