# 1) Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz

# sayi = int(input("Sayı giriniz "))
# if (sayi < 100) and (sayi > 50):
#     print(f"{sayi}, 50 ile 100 arasındadır")
# else:
#     print(f"{sayi}, 50 ile 100 arasında değildir")




# 2) Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz

# sayi = int(input("Sayı giriniz "))

# if (sayi > 0) and (sayi % 2 == 1):
#     print("Girilen sayı pozitif tek sayıdır")

# else:
#     print("Girilen sayı pozitif tek sayı değildir")




# 3) username ve parola bilgileriyle giriş kontrolü yapınız

# username = "hakan"
# password = "1234"

# girilenUsername = (input("Kullanıcı adınızı giriniz: "))
# girilenPassword = (input("Şifreyi giriniz: "))

# if girilenUsername == username:   
#     if girilenPassword == password:
#         print("Hoşgeldiniz")

# else:
#     print("Kullanıdı adı veya şifre hatalı")




# 4) Girilen 3 sayıyı büyüklük olarak karşılaştırınız

# sayi1 = int(input("1. sayıyı giriniz: "))
# sayi2 = int(input("2. sayıyı giriniz: "))
# sayi3 = int(input("3. sayıyı giriniz: "))

# if (sayi1 > sayi2) and (sayi1 > sayi3):
#     print(f"{sayi1} en büyük sayıdır")

# elif (sayi2 > sayi1) and (sayi2 > sayi3):
#     print(f"{sayi2} en büyük sayıdır")

# else: 
#     (sayi3 > sayi1) and (sayi3 > sayi2)
#     print(f"{sayi3} en büyük sayıdır")




# 5) Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız

# a) Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın
# b) ortalama 50 olsa bile final notu en az 50 olmalıdır 
# c) Finalden 70 alındığında ortalamanın önemi olmasın

# vize1 = float(input("Vize 1: "))
# vize2 = float(input("Vize 2: "))
# final = float(input("Final: "))
# vizeOrt = (vize1 + vize2) / 2
# finalOrt = final * 0.6
# ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)

# A)
# if (ortalama >= 50):
#     print(f"Öğrencinin ortlaması {ortalama} ve sınıfı geçti")
# else:
#     print(f"Öğrencinin ortlaması {ortalama} ve sınıfı geçemedi")

# B)
# if (ortalama >= 50):
#     if (final >= 50):
#         print (f"Öğrencinin ortlaması {ortalama} ve sınıfı geçti")
# else:
#     print(f"Öğrenci finalden {final} aldı ve sınıfı geçemedi")

# C)
# if (final >= 70):
#     print(f"Öğrenci finalden {final} aldı ve sınıfı direkt olarak geçti")
# else:
#     print(f"Öğrencinin ortalaması {ortalama} ve sınıfı ortlama notuyla geçti")

# 6) Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
zayif = 0-18.4
normal = 18.5-24.9
kilolu = 25.0-29.9
obez = 30.0-34.9

isim = (input("Adınız: "))
kg = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

kiloIndex = kg / (boy ** 2)

if (kiloIndex >= 0) and (kiloIndex <= 18.4):
    print(f"{isim} kilo endeksin {kiloIndex} ve kilo değerlendirmen zayıf")
elif (kiloIndex >= 18.5) and (kiloIndex <= 24.9):
    print(f"{isim} kilo endeksin {kiloIndex} ve kilo değerlendirmen normal")
elif (kiloIndex >= 25.0) and (kiloIndex <= 29.9):
    print(f"{isim} kilo endeksin {kiloIndex} ve kilo değerlendirmen kilolu")
elif (kiloIndex >= 30.0) and (kiloIndex <= 34.9):
    print(f"{isim} kilo endeksin {kiloIndex} ve kilo değerlendirmen obez")
else:
    print("Girilen bilgiler yanlış!")