HakanHesap = {
    "ad" : "Hakan Hakan",
    "hesapNo" : "123456789",
    "bakiye" : 3000,
    "ekHesap" : 1000
}

TalhaHesap = {
    "ad" : "Talha Saygılı",
    "hesapNo" : "127456789",
    "bakiye" : 2000,
    "ekHesap" : 2000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h)")
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz!")
            bakiyeSorgula(hesap)
def paraYatir(hesap, yatirilanMiktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["ekHesap"] < 2000):
        hesap["ekHesap"] + yatirilanMiktar
        print("Ek hesabınızdaki bakiyeniz eksik olduğu için yatırdığınız paranın bir kısmı ek hesabınıza yatırılmıştır")
        bakiyeSorgula(hesap)
    else:
        hesap["bakiye"] + yatirilanMiktar
        print("Paranız hesabınıza yatırılmıştır")
        bakiyeSorgula(hesap)
        

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesabınızda ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(HakanHesap, 1000)