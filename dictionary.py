sehirler = ["kocaeli","istanbul"]
plakalar = [41,34]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index("istanbul")])
# print(plakalar[sehirler.index("kocaeli")])

plakalar = {"kocaeli": 41,"istanbul":34}

# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

#bu şekilde listeye yeni elemanlar ekleyebiliriz
plakalar["rize"] = 53
plakalar["izmir"] = 35

ogrenciler = {
    100: {
        "Ad:": "Hakan",
        "Soyad": "Yaraş",
        "yas": 25,
        "notlar": [70,80,70]
    },
    101: {
        "Ad": "Erdem",
        "Soyad": "Kelkit",
        "yas": 21
    }
}
sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(sonuc)

