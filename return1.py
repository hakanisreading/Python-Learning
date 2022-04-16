import datetime

def yil():
    return datetime.datetime.now().year

def saat():
    return datetime.datetime.now().hour

def selamla():
    if (saat() < 12):
        return "Günaydın"
    elif (saat() > 12 and saat() < 18):
        return "İyi günler"
    elif (saat() > 18 and saat() < 21):
        return "İyi akşamlar"
    else:
        return "İyi geceler"

sonuc = selamla()
print(sonuc)