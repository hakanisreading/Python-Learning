diller = ["Python","C#","Java","Javascript","React"]
sonuc = diller
sonuc = type(diller)

#Listede sıfırdan ikiye kadar olan liste elemanlarını alır
sonuc = diller[0:2]

#listede 2 den sonsuza kadar tüm elemanları alır
sonuc = diller[2:]

# 3 dahil olmadan ondan önceki elemanlar gelir
sonuc = diller[:3]

# en sondaki elemanı verir
sonuc = diller[-1]

# -1 dahil olmadan -4 e kadar olan elemanları verir
sonuc = diller[-4:-1]

# Liste içindeki herhangi bir elemanı değiştirebiliriz
diller[0] = "Html"
diller[-1] = "Html"
sonuc = len(diller)

#bu da değiştirmenin farklı bir yöntemi
sonuc = diller + ["Angular","Vuejs"]

# Koşul ifadesiyle bir eleamnın listenin içinde olup olmadığını sorgulayabiliriz
if "Java" in diller:
    print("Değer listenin bir elemanı")

#Listenin bütün elemanlarını alt alta yazdırabiliriz
for x in diller:
    print(x)