msg = "Python Kursumuza Hoş Geldiniz. Ben Hakan Yaraş"

#upper komutu string ifadesindeki tüm karakterleri büyük harfe çevirir
sonuc = msg.upper()

#lower komutu string ifadesindeki tüm karakterleri küçük harfe çevirir
sonuc = msg.lower()

#title komutu string ifademizdeki her kelimenin ilk harfini büyük harf yapar
sonuc = msg.title()

#capitalize sadece cümlenin ilk harfini büyük harfe çevirir. Diğer kelimelerin baş harfleri büyükse onları da küçültür
sonuc = msg.capitalize()

#başına "is" gelen bütün komutlar soru sorar. Program da "true" veya "false" ile yanıt verir
sonuc = msg.islower()

#strip komutu string ifadesinde başta ve sonda fark etmeksizin tüm boşlukları siler
sonuc = "    abc ".strip

#split komutu string ifadesindeki her bir kelimeyi ayrı bir dizi olarak alır
#Bunun bize sağladığı yarar ise, her bir diziyi sıra numaralarına göre çağırabiliriz. Mesela 'print(sonuc[2])' yazarsak bize 'Hoş' dizisini gösterir
sonuc = msg.split()

#Eğer istersek özel olarak bizim belirttiğimiz karakterden de stringi parçalayabiliriz
sonuc = msg.split()

#Burda da tam tersi bir şekilde split ile ayırdığımız kelimeleri tekrardan join komutu ile birleştirebiliriz.
#Ayrıca join'den önce bir string ifadesiyle kelimelerin aralarında ne görüneceğine karar verebiliriz
sonuc = msg.split()
sonuc = "-".join(sonuc)

#Burada Geldiniz kelimesini programa aratıyoruz ve bize kaçıncı karakterden sonra başladığı bilgisini gösteriyor
index = msg.index("Geldiniz.")

#Bu komutlar ise string ifadesinin hangi harfle başladığını sorgular ve bize doğruluğa göre true veya false olarak cevaplar verir
sonuc = msg.startswith("P")
sonuc = msg.endswith("ş")

#Replace komutu bir kelimenin yerine başka bir kelimeyi yazdırmaya yarar
#Bunu birden fazla kez yapailiriz
sonuc = msg.replace("Hakan","Can")
sonuc = msg.lower().replace(" ","-").replace("ş","s").replace(".","").replace("ı","i")
print(sonuc)