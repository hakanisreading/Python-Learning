def tamBölenleriBul(sayi): 
    tamBolenler = []
    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler
print(tamBölenleriBul(655))