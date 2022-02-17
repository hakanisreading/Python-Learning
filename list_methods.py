sayilar = [1,5,8,9,3,45,77,5]
harfler = ["a","b","e","s","a","y"]

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

# append komutu listeye yeni bir eleman ekler
sayilar.append(10)

# bizim belirlediğimiz bir yere eleman eklemek için önce eklemek istediğimiz konumu sonra eklemek istediğimiz elemanı yazıyoruz
sayilar.insert(3,5)
sayilar.insert(-1,50)

# listenin en sonuna bir eleman eklemek istersek de önce listenin uzunluğunu alıyoruz sonra da eklemek istediğimiz elemanı yazıyoruz
sayilar.insert(len(sayilar),150)

# pop ve remove komutuyla listenin en sonundaki elemanı default olarak silebiliriz. Fakat parantez içine konum belirterek de istediğimiz karakteriz silebiliriz
sayilar.pop()
sayilar.pop(0)
harfler.remove("e")

# sarı veya alfabeyi düzenli olarak sıralamak için sort komutundan yararlanırız
sayilar.sort()
harfler.sort()

# sıraladığımız listeyi tersten yazdırmak istersek eğer reverse komutundan yararlanırız
sayilar.reverse()

# Belirtilen elemandan kaç tane olduğunu bulmak için count komutundan yararlanırız
# print(sayilar.count(5))
# print(harfler.count("a"))

# Belirtilen elemanın konumunu bulmak için index komutundan yararlanırız
print(sayilar.index(3))

# Listeyi tamamen silmek için de clear komutundan yararlanırız
print(sayilar.clear())

sonuc = sayilar
print(sonuc)
print(harfler)