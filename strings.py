ad = "Hakan"
soyad = "Yaraş"
yas = "19"

msj = "Benim adım " + ad + " soyadım " + soyad + "." + " Yaşım ise " + yas

#Msj değişkeni içinde kaç karakter olduğunu gösterir
karakterSayisi = len(msj)

print(msj[0])
print(msj[1])
print(msj[-1])
print(msj[karakterSayisi -1])

#Burada belirtilen sayılara kadar olan karakterleri toplu bir şekilde gösterir
print(msj[0:10])
print(msj[11:16])
print(msj[0:50])

#Burada 2 ile belirtilen ifade soldan sağa ikişer ikişer gitmesini ve aradaki karakterleri almamasını sağlar
print(msj[0:50:2])

#Bu kodumuz ise string ifademizi tersten yazdırır
print(msj[::-1])