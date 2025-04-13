# Tuple  are like immutable list

my_tuple = (1,2,3,4,5)
# my_tuple[1]= 'z' # TypeError: 'tuple' object does not support item assignment

print(my_tuple[1])
print(5 in my_tuple)

# if you don't need to change the list, then we can use tuple. Making code safer and predictable but less flexible
# we cannot run things like reverse, but they are faster than list, and we don't need a list to change we use tuple
# For example when we want to use latitude and longitude.


user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.items())
print(user[(1,2)])

# slice tuple
new_tuple = my_tuple[1:2]

# x  = my_tuple[0]
# y = my_tuple[1]



print(new_tuple) # (2,) because has a single item

# x, y, z, *other = (1,2,3,4,5);

# print(other)

print(my_tuple.count(5)) # 1
print(my_tuple.index(5)) # 4
print(len(my_tuple)) # 5



