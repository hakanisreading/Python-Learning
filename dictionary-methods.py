opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}
# Sözlük içinden bir eleman göstermek
# sonuc = opelObj["marka"]
# sonuc = opelObj.get("marka")
# print(sonuc)

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")

# for x in opelObj:
#     print(x)

# Sözlük içindeki tüm elemanları gösterir
# for x in opelObj.values():
#     print(x)

# for x,y in opelObj.items():
#     print(x,y)

# Aradığımız nesnenin liste içinde olup olmadığını sorgulayabiliriz

#true
# sonuc = "marka" in opelObj
# print(sonuc)

# #false
# sonuc = "markaa" in opelObj
# print(sonuc)

# Burda liste içindeki tüm satırları sayar ve bize kaç elemanlı olduğunu gösterir
# sonuc = len(opelObj)
# print(sonuc)

# Listeye yeni bir dizi eklemek
# opelObj["renk"] = "kırmızı"

# Listeden bir dizi silmek 
# opelObj.pop("renk")
# print(opelObj) 

# sözlükten dizi silmenin başka yöntemi
# del opelObj["marka"]
# print(opelObj)

# direkt olarak diziyi silmek
# del opelObj
# print(opelObj)

# Liste içindeki tüm elemanları silmek
# opelObj.clear()
# print(opelObj)

# kopyalama yöntemiyle liste içindeki bir elemanı değiştirmek
# obj = opelObj.copy()
# obj ["marka"] = "Mazda"
# print(obj)

# Referans almadan olduğu gibi kopyalamak
# obj = opelObj.copy()

# Liste içerisindeki bir elemanı değiştirmek
# opelObj.update({
#     "marka": "BMW",
#     "renk": "Kırmızı"
# })
# print(opelObj)