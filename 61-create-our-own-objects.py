# Object Oriented Programming
# --------------------------------------

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is running")

# --------------------------------------

player1 = PlayerCharacter("Jason", 44)
player2 = PlayerCharacter("Josh", 21)
player2.attack = 50

print(player1.name)
print(player2.name)
player1.run()
player2.run()

print(player2.attack)

