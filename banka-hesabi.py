class BankAccount:
    def __init__(self, name,):
        self.name = name
        self.balance = balance = 0.0
    # Anlık para miktarını döndürür
    def getBalance(self):
        return self.balance
    # Yeni para miktarını ekler
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    # Çekilen para miktarını çıkarır
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# Hakan Yaraş'ın hesabındaki para mikarını gösterir
hesap = BankAccount("Hakan Yaraş")
print(hesap.getBalance())

# Hesaba 1000 TL ekler
hesap.deposit(1000)
print(hesap.getBalance())

# Hesaptan 500 TL çekler
hesap.withdraw(500)
print(hesap.getBalance())