class OnlineShopAccount:
    def __init__(self, username, balance=0, shopcart=[]):
        self.username = username
        self.balance = balance
        self.shopcart = shopcart

    def add_funds(self, amount):
            self.balance += amount

    def buy_item(self, item_name, price):
        if price > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= price
            self.shopcart.append(item_name)

    def refund(self, item_name, amount):
            self.balance += amount
            self.shopcart.remove(item_name)

    def show_balance(self):
        print(f"Current balance: {self.balance}")

user = OnlineShopAccount("Walter White", 100)
user.add_funds(50)
user.show_balance()
user.buy_item("methane", 120)
user.buy_item("fent", 200)
user.add_funds(300)
user.buy_item("fent", 200)
user.refund("fent", 200)
user.show_balance()