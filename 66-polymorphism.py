# Object-Oriented Programming
# Polymorphism

class User(object):
    # def __init__(self, name):
    #     self.name = name

    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        # super().__init__("Merlin")

    def attack(self):
        print(f"{self.name} attacks with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        # super().__init__("Merlin")

    def attack(self):
        print(f"{self.name} attacks with arrows:  {self.num_arrows}")




wizard1 = Wizard('Merlin', 50)

archer1 = Archer('Robin', 30)

# Example 1
# def player_attach(char):
#     char.attack()
#
# player_attach(wizard1)
# player_attach(archer1)

# Example 2
for char in [wizard1, archer1]:
    char.attack()