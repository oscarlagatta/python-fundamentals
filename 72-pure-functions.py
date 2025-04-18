# Pure Functions
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list
#
#
# print(multiply_by2([1, 2, 3])) # [2, 4, 6]
#
#
# # The following has side effects because we don't know what print is going to do
# def multiply_by21(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return print(new_list)
#
#
# # The following has side effects
# new_list = []
# def multiply_by22(li):
#     for item in li:
#         new_list.append(item * 2)
#     return new_list
#
# new_list = '' # this will cause an error AttributeError: 'str' object has no attribute 'append'
# print(multiply_by22([1, 2, 3])) # [2, 4, 6]


# class Magician:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attack(self):
#          return f'{self.name} attacks with power of {self.power}'
#
# wizard = Magician('Merlin', 50)
# print(wizard.attack())

wizard2 = {
    'name': 'Merlin',
    'power': 50,
}

def attach(character):
    print(
        f'{character["name"]} is attacking'
    )

attach(wizard2)