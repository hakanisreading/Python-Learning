# all fonksiyonu kendisine gelen liste elemanları içerisindeki bütün elemanlara bakar ve hepsinin true olduğu durumlarda true değeri gönderir
sonuc = all([True,True,True])

# any fonksiyonu ise eğer listede tek bir true değer var ise true değer döndürür
sonuc = any([True,False,False])

sayilar = [0,1,2,3,4,5,6,7,8]

# listede 0 olduğu için all fonksiyonu false değer verir
sonuc = all([bool(sayi) for sayi in sayilar])

# listede 0 dahi olsa any fonksiyonu true değer döndürür
sonuc = any([bool(sayi) for sayi in sayilar])

# listedeki sayıların mod1 ini aldığımızda yalnızca tek sayıları alacağı için (0 dahil olmaz) true değer döndürür
sonuc = all([bool(sayi) for sayi in sayilar if sayi % 2 == 1])

# Burada listedeki elemanların hepsi çift sayı mı diye sorulur ve all fonksiyonu false değer döndürür
sonuc = all([sayi % 2 == 0 for sayi in sayilar])

# Burada listedeki elemanların hepsi çift sayı mı diye sorulur ve any fonksiyonu true değer döndürür
sonuc = any([sayi % 2 == 0 for sayi in sayilar])


kisiler = ["ali","ahmet","hakan"]

# Kisiler listesindeki bütün isimer a harfi ile mi başlıyor diye sorgulama yapar ve all fonksiyonu false değer döndürür
sonuc = all([kisi[0] == "a" for kisi in kisiler])

# Kisiler listesindeki bütün isimer a harfi ile mi başlıyor diye sorgulama yapar ve any fonksiyonu true değer döndürür
sonuc = any([kisi[0] == "a" for kisi in kisiler])
print(sonuc)
