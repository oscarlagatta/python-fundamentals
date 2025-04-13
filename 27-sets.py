# set
my_set = {1,2,3,4,5,5}
print(my_set) # returns only unique values # {1, 2, 3, 4, 5}
my_set.add(100)
my_set.add(2)
print(my_set) # returns only unique values # {1, 2, 3, 4, 5, 100}

my_list = [1,2,3,4,5,5]
# return a collection with unique values
set(my_list) # we don't want to have e.g. duplicate users, or emails.
print(my_list) #

my_set1 = {1,2,3,4,5,5}
# print(my_set1[0]) # does not support indexing
print(1 in my_set1) # True
print(len(my_set1))

new_set = my_set1.copy()
# we can convert into a list
print(list(my_set1))
print(new_set)



