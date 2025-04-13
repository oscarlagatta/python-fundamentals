# iterable can be a list, dictionary, tuple, set, string

# for item in (1,2,3,4,5):
#     for x in ['a', 'b','c']:
#         print(item, x)

users = {
    'name': 'Golem',
    'age': 50,
    'can_swim': False
}

for item in users.items():
    key, value = item
    print(key, value)

for key, value in users.items():
    print(key, value)

for item in users.values():
    print(item)

for item in users.keys():
    print(item)

