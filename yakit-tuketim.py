benzin = 15.40
dizel = 15.60

yakitTipi = str(input("Aracınızın yakıt tipini giriniz (benzin, dizel): "))
neKadarYakiyor = float(input("Aracınız 100 km mesafede kaç litre yakıyor? "))

benzinMasraf = neKadarYakiyor * benzin
dizelMasraf = neKadarYakiyor * dizel

if yakitTipi == "benzin":
    print(f"Aracınızın 100 km mesafedeki yakıt masrafı: {benzinMasraf}")

elif yakitTipi == "dizel":
    print(f"Aracınızın 100 km mesafedeki yakıt masrafı: {dizelMasraf}")

else:
    print("Girilen bilgiler yanlış!")

sorulanMesafe = float(input("Merak ettiğiniz mesafeyi giriniz: "))
toplamYakitTuketimi = sorulanMesafe * (neKadarYakiyor / 100)

if yakitTipi == "benzin":
    toplamYakitUcreti = benzin * toplamYakitTuketimi
elif yakitTipi == "dizel":
    toplamYakitUcreti = dizel * toplamYakitTuketimi
else:
    print("Girilen bilgiler yanlış!")

print(f"Sorduğunuz mesafedeki toplam yakıt ücretiniz: {toplamYakitUcreti}")
