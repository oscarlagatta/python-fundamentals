# map, filter, zip, reduce

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

# print(multiply_by2([1, 2, 3, 4, 5]))

# map creates a new list out of the existing list my_list

my_list = [1, 2, 3]

def multiply_by21(item):
    return item * 2

# print(list(map(multiply_by2, [1, 2, 3]))) # [2, 4, 6]
print(list(map(multiply_by21, my_list))) # [2, 4, 6]

new_list2 = map(multiply_by21, my_list)
print(list(new_list2))

