# Object-Oriented Programming
# Inheritance

class User(object):
    # def __init__(self, name):
    #     self.name = name

    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__("Merlin")

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

# archer1 = Archer('Robin', 100)
# print(wizard1.sign_in())
# wizard1.attack()
# archer1.attack()

print(isinstance(wizard1, User))
print(isinstance(wizard1, object)) # wizard1 gets from Wizard class, from the User class, and from the object class
