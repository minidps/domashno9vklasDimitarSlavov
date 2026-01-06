class Player:
    def __init__(self, name, health=100, energy=100):
        self.name = name
        self.health = health
        self.energy = energy

    def attack(self):
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0
            print("Not enough energy to attack!")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            print("You died!")

    def heal(self):
        self.health += 20
        if self.health > 100:
            self.health = 100

    def regain_energy(self):
        self.energy += 15
        if self.energy > 100:
            self.energy = 100

    def status(self):
        print(f"Player: {self.name}, Health: {self.health}, Energy: {self.energy}")

player1 = Player("mini212131")
player1.status()
player1.attack()
player1.status()
player1.take_damage(30)
player1.status()
player1.heal()
player1.status()
player1.regain_energy()
player1.status()