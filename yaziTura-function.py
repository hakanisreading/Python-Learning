import random

def yaziTuraAt():
    sayi = random.random()

    if sayi > 0.5:
        return ("Tura")
    else:
        return ("Yazı")

print(yaziTuraAt())