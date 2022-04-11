import random

sayi = random.randint(1,100)
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print("Tebrikler bildiniz")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")
    if hak == 0:
        print(f"Hakkınız bitti :( Tutulan sayı {sayi}")