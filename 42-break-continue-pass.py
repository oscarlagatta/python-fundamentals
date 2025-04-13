# break, continue, pass

my_list =[1,2,3]
for item in my_list:
    print(item)
    continue


i = 0
while i < len(my_list):
    i += 1
    print(my_list[i])
    continue


# be careful with where you put the continue

for item in my_list:
    continue
    print(item) # wont reach this line the continue will send back to the for loop

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])