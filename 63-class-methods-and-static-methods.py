# Object-Oriented Programming
# Attributes and Methods
# --------------------------------------

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if self.membership:
            self.name = name
            self.age = age

    def run(self):
        print(f"{self.name} is running")

    def shout(self):
            print(f"my name is {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)

    @staticmethod
    def adding_things1(num1, num2):
        return num1 + num2

    @staticmethod
    def is_member(name):
        return True


# --------------------------------------

player1 = PlayerCharacter("Jason", 44)
player2 = PlayerCharacter("Josh", 21)

player1.from_birth_year('Teddy', 1990)
print(player1.age)

player3 = PlayerCharacter.adding_things(1, 2)
# print(PlayerCharacter.adding_things(1, 2))
print(player3.name)
print(player3.age)



# player2.attack = 50

print(player1.name)
print(player2.name)
player1.run()
player2.run()

# print(player2.attack)

help(player1)

# Help on PlayerCharacter in module __main__ object:
#
# class PlayerCharacter(builtins.object)
#  |  PlayerCharacter(name, age)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  run(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables
#  |
#  |  __weakref__
#  |      list of weak references to the object

player2.shout()
