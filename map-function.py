sayilar = [1,-2,-5,7,-9]
str_sayilar = ["1","2","5","7","9"]
isimler = ["ali","deniz","emel","çınar"]
kullanicilar = [
    {"ad":"Hakan", "Soyad":"Yaraş"},
    {"ad":"Hasan", "Soyad":"Yaraş"}
]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi ** 2)

# print(sonuc)

# def kareAl(sayi):
#     return sayi ** 2

# listedeki sayıların karesini alır
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))

# string ifadesi olan sayıları int türüne çevirir
sonuc = list(map(int, str_sayilar))

# + veya - işareti olan sayıları işaretsiz alır
sonuc = list(map(abs, sayilar))

# listedeki elemanları float tipinde gösterir
sonuc = list(map(float, sayilar))

# listedeki string elemanlarının uzunluklarını gösterir
sonuc = list(map(len, isimler))

# listedeki string elemanlarının baş harflerini büyültür
sonuc = list(map(str.capitalize, isimler))

# listedeki string elemanlarının baş harflerini küçültür
sonuc = list(map(str.lower, isimler))

# Liste içerisinden belirli bir kısmı alır
sonuc = list(map(lambda x: x["ad"], kullanicilar))
sonuc = list(map(lambda x: x["Soyad"], kullanicilar))
print(sonuc)