# Doğru değerler girilene kadar kullanıcıdan değer girmesi tekrar tekrar istenir. 
while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)

    # Sıfıra bölme hatasında bu except bloğu çalışır
    except ZeroDivisionError:
        print("Sıfır girilemez!")

    # # Sayısal değer girilmediğinde bu blok çalışır
    except ValueError:
        print("X ve Y sayısal bir değer olmalıdır")

    # Bu şekilde birden fazla hata mesajına aynı mesajı verdirebiliriz ve hatanın nedenini gösterebiliriz
    except (ZeroDivisionError, ValueError) as e:
        print("Hata oluştu!")
        print(e)

    except Exception as e:
        print("Bilinmeyen bir hata oluştu!")
        print(e)
    # Doğru değerler girilirse else çalışır ve program durdurulur
    else:
        break
    # Kodumuzda hata olsun veya olmasın finally bloğu her türlü çalışır
    finally:
        print("Finally bloğu çalıştı")