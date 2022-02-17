"""Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız"""

pi = 3.14

r = float(input("Yarı çap: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

result = "Alan: " + str(alan) + " Çevre: " + str(cevre)
print(result)