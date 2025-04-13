# Dictionary
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print('basket' in user.keys())
print('hello' in user.values())
print(user.items())
print('size' in user)
# user.clear()
user2 = user.copy()
# print(user.clear())
# print(user2)
# print(user)


print(user.popitem())
print(user)

# updated
print(user.update({'age': 55}))
print(user)