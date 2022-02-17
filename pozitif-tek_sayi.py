# Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz

sayi = int(input("Sayı giriniz "))

if (sayi > 0) and (sayi % 2 == 1):
    print("Girilen sayı pozitif tek sayıdır")

else:
    print("Girilen sayı pozitif tek sayı değildir")
