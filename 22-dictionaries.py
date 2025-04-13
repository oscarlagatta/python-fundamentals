# Dictionary

dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}

print(dictionary['b']) # hello
print(dictionary)


my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4,5,6],
        'b': 'hello',
        'x': True
    }
]

print(my_list[0]['a'][2])
print(my_list[1]['a'][1])