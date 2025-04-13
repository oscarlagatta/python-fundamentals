# set
# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}

# # .difference()
# print(my_set.difference(your_set)) # {1, 2, 3}
# # .discard
# my_set.discard(5)
# print(my_set) # {1, 2, 3, 4}
# difference_update
# print(my_set.difference_update(your_set))
# print(my_set)
#
# print(my_set.intersection(your_set))
# print(my_set)
#
# print(my_set.isdisjoint(your_set))

# new_set = my_set.union(your_set)
# new_set = my_set | your_set # shortcut for the previous line
# print(new_set)
# print(my_set)
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))


