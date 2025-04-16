# Object-Oriented Programming
# Introspection

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__(f'{name}@gmail.com')

    def attack(self):
        print(f"{self.name} attacks with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        super().__init__(f'{name}@gmail.com')

    def attack(self):
        print(f"{self.name} attacks with arrows:  {self.num_arrows}")




wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 30)

print(dir(wizard1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'attack', 'email', 'name', 'power', 'sign_in']


