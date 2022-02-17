# a = 5
# b = 10
# c = 20

# a, b, c = 5, 10, 20

# Değişkenlerin yerini değiştirmek
# a, b = b, a

# aritmetik işlemler
# Burda aslında amacımız a ile 5 i toplamak sonra sonucu tekrar a ya aktarmaktır
# a += 5    # a = a+5


# a -= 5    # a = a-5
# a *= 5    # a = a*5
# a /= 5    # a = a/5
# a %= 5    # a = a%5
# a **= 5    # a = a**5
# a //= 5    # a = a//5

# burda değişken sayısı operatör sayısına eşit olmalıdır. aksi halde programımız hata verir
# bir operatöre birden fazla değişken atamak istersek de o operatörün soluna * koymalıyız
# yani aşağıda yapılan işlem a = 1, b = 2, c = 3,4,5,6
# values = (1, 2, 3, 4, 5, 6)
# a, b, *c = values
# a, *b, c = values
# *a, b, c = values

# print(a, b, c)