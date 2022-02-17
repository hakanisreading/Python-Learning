print("Kaç km yol gittiniz?")
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)

print (str(mesafeMil) + " mil yol gittiniz")
