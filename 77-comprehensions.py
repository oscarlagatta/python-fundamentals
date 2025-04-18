# list, set, dictionary comprehensions
# my_list = []
# for char in 'hello':
#     my_list.append(char)

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
#
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# Sets

my_list_set = {char for char in 'hello'}
my_list2_set = {num for num in range(0,100)}
my_list3_set = {num*2 for num in range(0,100)}

# print(my_list_set)
# print(my_list2_set)
# print(my_list3_set)

simple_dic = {'a':1, 'b':2, 'c':3}

my_dic = {key: value**2 for key,value in enumerate(range(0,10))}
my_dic2 = {key: value**2 for key,value in simple_dic.items()}
my_dic3 = {key: value**2 for key,value in simple_dic.items() if value % 2 == 0}
my_dic4 = {num: num*2 for num in [1,2,3,4,5]}

# print(my_dic)
# print(my_dic2)
# print(my_dic3)
# print(my_dic4)

# Exercise

some_List = ['a', 'b', 'c', 'b', 'd', 'e', 'm' ,'n','n']

duplicates = list(set([x for x in some_List if some_List.count(x) > 1]))

print(duplicates)


