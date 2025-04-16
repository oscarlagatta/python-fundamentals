
class User(object):

    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power


    def attack(self):
        print(f"{self.name} attacks with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows


    def attack(self):
        print(f"{self.name} attacks with arrows:  {self.num_arrows}")

    def run(self):
        print(f"{self.name} runs fast")

class HybridBorg(Wizard, Archer):
    pass

hb1 = HybridBorg('Borgie', 50)
print(hb1.run())
print(hb1.attack())
print(hb1.sign_in())