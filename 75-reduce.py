# map, filter, zip, reduce
# reduce

from functools import reduce


my_list = [1, 2, 3]
your_list = [10,20,30]
their_list = [5,4,3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))

"""
Result
0 1
1 2
3 3
6
"""

print(reduce(accumulator, my_list, 10))

"""
10 1
11 2
13 3
16
"""


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_first_letter(name):
    return name.capitalize()
print(list(map(capitalize_first_letter, my_pets)))

def capitalize(name):
    return name.upper()
print(list(map(capitalize, my_pets)))



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def above_threshold(score):
    return score > 50
print(list(filter(above_threshold, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator2(acc, item):
    return acc + item

print(reduce(accumulator2, (my_numbers + scores), 0))
