class Toy:
    def __init__(self, color, age):
        self.age = age
        self.color = color

    def __str__(self):
        return f"I am a {self.color} toy, and I am {self.age} years old"

    def __len__(self):
        return 5

    def __del__(self):
        print("I am being deleted")

    def __call__(self):
        print("Yess I am being called")



action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))

# <__main__.Toy object at 0x000002A06D097CB0>
# <__main__.Toy object at 0x000002A06D097CB0>

# After modifiying the Toy class
#     def __str__(self):
#         return f"I am a {self.color} toy, it is {self.age} years old"
print(action_figure.__str__())
print(str(action_figure))

# I am a red toy, it is 0 years old
# I am a red toy, it is 0 years old

print(len(action_figure))