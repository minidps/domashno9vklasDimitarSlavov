class Wallet:
    currency = "EUR"
    balance = 0
    def add_money(self,amount):
        self.balance += amount
    
    def spend_money(self,amount):
        if amount > self.balance:
            print("You dont have that much money!")
        else:
            self.balance -= amount
    
    def show_balance(self):
        print(f"Balance: {self.balance} {self.currency}")
    
poorGuy = Wallet()
poorGuy.currency = "BGN"
poorGuy.balance = 3
poorGuy.add_money(10)
poorGuy.show_balance()
poorGuy.spend_money(300)
poorGuy.show_balance()

richGuy = Wallet()
richGuy.currency = "USD"
richGuy.balance = 1000000
richGuy.add_money(500)
richGuy.show_balance()
richGuy.spend_money(300)
richGuy.show_balance()