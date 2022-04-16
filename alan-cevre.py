def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    return f"Alan: {alan} Çevre: {cevre}"
print(hesapla(5,7))