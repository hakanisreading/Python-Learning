sayilar = [1,5,7,45,25,89]
harfler = ["a","v","h","s"]
isimler = ["ahmet","ismail","ada","sena"]
urunler = [
    {"title":"iphoneX","price":5000},
    {"title":"iphoneXR","price":6000},
    {"title":"iphone11","price":7000}
]

# sayılar listesindeki en küçük elemanı verir
sonuc = min(sayilar)

# sayılar listesindeki en büyük elemanı verir
sonuc = max(sayilar)

# harfler listesinin en küçük elemanını (a) verir
sonuc = min(harfler)

# harfler listesinin en büyük elemanını (v) verir
sonuc = max(harfler)

# alfabetik sıraya göre ilk hangi harf ile başlıyorsa o ismi getirir
sonuc = min(isimler)

# alfabetik sıraya göre en son hangi harf ile başlıyorsa o ismi getirir
sonuc = max(isimler)

# En az harfi olan isimde kaç harf olduğunu bulur
sonuc = min([len(isim) for isim in isimler])

# En fazla harfi olan isimde kaç harf olduğunu bulur
sonuc = max([len(isim) for isim in isimler])

# isimler listesindeki en uzun ismi yazar
sonuc = max(isimler, key=lambda n: len(n))

# isimler listesindeki en kısa ismi yazar
sonuc = min(isimler, key=lambda n: len(n))

# urunler listesinde fiyatı en düşük olan ürünü yazar
sonuc = min(urunler, key=lambda urun: urun["price"])
sonuc = min(urunler, key=lambda urun: urun["price"])["title"]

# urunler listesinde fiyatı en yüksek olan ürünü yazar
sonuc = max(urunler, key=lambda urun: urun["price"])["title"]

# for düngüsüyle yapmak isteseydik:
max = 0

for urun in urunler:
    if urun["price"] > max:
        max = urun["price"]


print(max)