sayilar = [34,2,5,7,98]

# Sayılar listesindeki sayıların toplamını verir
sonuc = sum(sayilar)

# bu şekilde ekleme de yapabiliriz
sonuc = sum(sayilar,10)

urunler = [
    {"title":"iphoneX","price":5000,"isactive":True},
    {"title":"iphoneXR","price":6000},
    {"title":"iphone11","price":7000},
    {"title":"iphone11 pro","price":0}
]

# urunler listesindeki ürünlerin fiyatları toplamını alır
sonuc = sum([urun["price"] for urun in urunler])

# Listedeki bütün ürünlerin fiyatlarının ortalamasını alır
toplamFiyat = sum([urun["price"] for urun in urunler])
sonuc = toplamFiyat / len(urunler)

# listemizde satışta olmayan ve fiyatı 0 olarak görünen bir ürün var ve onu ortalamaya dahil etmememiz gerekiyor bu yüzden böyle bir yöntem kullanabiliriz
toplamFiyat = sum([urun["price"] for urun in urunler])
urunAdeti = len([urun for urun in urunler if urun["price"]>0])
sonuc = toplamFiyat / urunAdeti

# ya da "isactive" kullanarak o ürünün o an satışta olup olmadığını belirtebiliriz

# Round fonksiyonu yuvarlama yapmak için kullanılır
sonuc = round(10.2)
sonuc = round(10.6)

# Ondalıklı kısmı kaybetmeden sadece belirlediğimiz basamağını almak istersek yanına görmek istediğimiz basamak sayısını virgülle yazarız
sonuc = round(10.424242,2)
print(sonuc)