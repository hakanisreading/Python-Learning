import os 
import datetime

result = dir(os)

# İşletim sistemini öğrenmek için kullanılır
result = os.name

# Dosyayı belirtilen dizine taşır
os.chdir("C:\\")

# Bulunduğumuz klasörü gösterir
result = os.getcwd()

# yeni klasörü olusturur
os.mkdir("newdirectory")

# Birden fazla klasör oluşturur
os.makedirs("newdirectory/newdirectory2")

# Klasörün ismini değiştirir
os.rename("newdirectory/newdirectory2","newdirectory/yeni klasör")

# Bulunduğumuz dizindeki klasörleri gösterir
result = os.listdir()

# Bulunduğumuz dizindeki klasörleri gösterir
result = os.listdir("C:\\")

# Bulunulan dizindeki Python dosyalarını gösterir
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

# Dosyanın durumunu gösterir
result = os.stat("bankamatik.py")
result = result.st_size / 1024

# Dosyanın oluşturulma tarihini gösterir
result = datetime.datetime.fromtimestamp(result.st_ctime)

# Dosyanın son erişilme tarihini gösterir
result = datetime.datetime.fromtimestamp(result.st_atime)

# Dosyanın son değiştirilme tarihini gösterir
result = datetime.datetime.fromtimestamp(result.st_mtime)

# Not defterini açar
os.system("notepad.exe")

# Klasörü siler
os.rmdir("yeni dizin")

# Klasörü alt dizinleriyle birlikte siler
os.removedirs("newdirectory/newdirectory")

# Dsoyanın tam konumunu gösterir
result = os.path.abspath("bankamatik.py")

# Dsoyanın tam konumu verilen bir dosyanın dizin ismini alır
result = os.path.dirname("C:/Users/hyara/Desktop/python_temelleri/bankamatik.py")

# Bu kod üstteki iki kodun birleşimidir. Dosyanın bulunduğu dizini gösterir
result = os.path.dirname(os.path.abspath("bankamatik.py"))

# Belirttiğimiz dosyanın o dizinde olup olmadığını gösterir
result = os.path.exists("bankamatik.py")

# Verilen adresin klasör olup olmadığını gösterir
result = os.path.isdir("C:/Users/hyara/Desktop/python_temelleri")

# Verilen adresin dosya olup olmadığını gösterir
result = os.path.isfile("C:/Users/hyara/Desktop/python_temelleri/bankamatik.py")

# Yazılan dizinde öyle bir klasör olup olmadığını kontrol eder
result = os.path.join("C:\\", "deneme","deneme2")

# Path bilgilerini böler
result = os.path.split("C\\deneme")

# Dsoyanın ismiyle uzantısını ayırır
result = os.path.splitext("bankamatik.py")
# result = result[0]
result = result[1]

print(result)