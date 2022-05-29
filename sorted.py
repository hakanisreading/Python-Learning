sayilar = [1,54,23,76,34,24]

# sayilar.sort()
sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((1,54,23,76,34,24))

users = [
    {"username":"hakan","tweets":["tweet1","tweet2"],"email":"info@gmail.com"},
    {"username":"talha","tweets":[]},
    {"username":"erdem","tweets":["tweet1"],"name":"","phone":"65465465465"}
]

# Users listesindeki kullanıcıları en az değeri olandan en çok değeri olana doğru sıralar
sonuc = sorted(users, key=len)

# Users listesindeki kullanıcıları en çok değeri olandan en az değeri olana doğru sıralar
sonuc = sorted(users, key=len, reverse=True)

# Listedeki elemanları username lere göre alfabetik sıraya dizer
sonuc = sorted(users, key=lambda user: user["username"])

# listede en az tweeti olandan en çok tweeti olana doğru sıralar
sonuc = sorted(users, key=lambda user: len(user["tweets"]))

kurslar = [
    {"title":"python kursu","students":25000},
    {"title":"web geliştirme kursu","students":35000},
    {"title":"javascript kursu","students":5000}
]

# kurslar listesinde en az öğrencisi olandan en çok öğrencisi olana doğru sıralama yapar
sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])

# En popüler kurs hangisiyse o en başa gelir
sonuc = sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True)

# En popüler olandan en az popüler olana doğru sadece kurs isimlerini sıralar
sonuc = map(lambda kurs: kurs["title"],sorted(kurslar, key=lambda kurs: kurs["students"],reverse=True))
print(list(sonuc))
