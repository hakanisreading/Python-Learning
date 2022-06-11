# Datetime modülünden yalnızca datetime classını çeker
from datetime import datetime

# Datetime modülünden yalnızca timedelta classını çeker
from datetime import timedelta

# Datetime modülünden yalnızca date classını çeker
# from datetime import date

# Datetime modülünden yalnızca time classını çeker
# from datetime import time

# Modül içerisindeki bütün klaslara ulaşabilirsiniz
# import datetime

# Güncel tarih ve saati gösterir
result = datetime.now()

simdi = datetime.now()
simdi = datetime.today()

# Yıl bilgisini gösterir
result = simdi.year

# Ay bilgisini gösterir(yılın kaçıncı ayı şeklinde)
result = simdi.month

# Ayın kaçıncı günü şeklinde günü gösterir
result = simdi.day

# Saat bilgisini gösterir
result = simdi.hour

# Dakika bilgisini gösterir
result = simdi.minute

# Saniye bilgisini gösterir
result = simdi.second

# Tarih ve saat bilgisini daha ayrıntılı şekilde gösterir
result = datetime.ctime(simdi)

# Sadece yıl bilgisini verir
result = datetime.strftime(simdi,"%Y")

# Sadece saat bilgisini verir
result = datetime.strftime(simdi,"%X")

# Sadece gün bilgisini verir
result = datetime.strftime(simdi,"%d")

# Gün bilgisini string olarak verir
result = datetime.strftime(simdi,"%A")

# Ay bilgisini string olarak verir
result = datetime.strftime(simdi,"%B")

# Aynı anda birden fazla özelliği kullanabiliriz
result = datetime.strftime(simdi,"%Y %B %A")

# Split parametresiyle string ifadesi içindeki tarihi gün ay yıl bilgisine ayırabiliriz
# t = "12 Ağustos 2022"
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)

# Burada kullanabilecek olduğumuz bir objemiz var bunun üzerinden istediğimiz her türlü işlemi yapabiliriz
t = "12 August 2022 hour 10:12:45"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
result = result.year

birthday = datetime(2002,8,12,12,30,30)

# Girilen tarih bilgisi saniye cinsinden verilir
result = datetime.timestamp(birthday)
result = datetime.fromtimestamp(result) # saniyeden datedime'a çevirir

# Bilgisayarlar için milat bilgisi 1970 olduğu için o şekilde gösterilir
result = datetime.fromtimestamp(0)

# İki tarih arasındaki farkı bu şekilde alabiliriz
result = simdi - birthday #timedelta

# Timedeltadan getirilen toplam gün bilgisi
# result = result.days

# Timedeltadan getirilen toplam saniye bilgisi
# result = result.seconds

# Timedeltadan getirilen toplam milisaniye bilgisi
result = result.microseconds

# Girilen tarihe gün ekler
print(simdi)
result = simdi + timedelta(days = 10)
result = simdi + timedelta(days = 730)

# Girilen tarihten gün çıkarır
result = simdi - timedelta(days = 730)

print(result)