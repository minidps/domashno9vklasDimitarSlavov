class BankAccount:
    name = ""
    balance = 0
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("You are overestamating yourself!!!")
        else:
            self.balance -= amount
    
poorGuy = BankAccount()
poorGuy.name = "Pesho"
poorGuy.balance = 3
poorGuy.deposit(10)
print(poorGuy.balance)
poorGuy.withdraw(300)
print(poorGuy.balance)

richGuy = BankAccount()
richGuy.name = "Bergman"
richGuy.balance = 1000000
richGuy.deposit(500)
print(richGuy.balance)
richGuy.withdraw(300)
print(richGuy.balance)