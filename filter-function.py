yaslar = [5,12,18,24,45]
sayilar = [0,1,2,5,7,8,9,4]
users = [
    {"username":"hakanyaraş", "tweets":["tweet 1","tweet2"]},
    {"username":"hasanyaraş", "tweets":[]},
    {"username":"harunyaraş", "tweets":["tweet 1"]}
]

# 18 yaişında veya büyük olan yaşları alır
def yetiskinmi(x):
    if x < 18:
        return False
    else:
        return True
sonuc = list(filter(yetiskinmi, yaslar))

# 18 yaşından büyük olanları lambda methodu ile alır
sonuc = list(filter(lambda x: x >= 18, yaslar))

# sayılar listesindeki çift sayıları alır
sonuc = list(filter(lambda x: x % 2 == 0, sayilar))

# isimler listesinde baş harfi a olan isimleri alır
isimler = ["çınar","yiğit","sena","ada","ali"]
sonuc = list(filter(lambda n: n[0] == "a", isimler))
filteredResult = filter(lambda n: n[0] == "a", isimler)

# isimler listesindeki bütün elemanları büyük harfe çevirir
sonuc = list(map(lambda n: n.upper(), filteredResult))

#map methodu ile listedeki bütün elemanlar üzerinde işlem yaparız. ancak belirli elemanlar üzerinde işlem yapmak istediğimizde filter methodunu kullanmalıyız

# en az 1 tweet atmış kullanıcıları gösterir
sonuc = list(filter(lambda u: len(u["tweets"])>0, users))

# en az 1 tweet atmış kullanıcıları büyük harfe çevirerek gösterir
sonuc = list(map(lambda u: u["username"].upper(), filter(lambda u: len(u["tweets"])>0, users)))

# yukarıdaki işlemin başka bir yöntemi
sonuc = [user["username"].upper() for user in users if len(user["tweets"]) > 0]
print(sonuc)