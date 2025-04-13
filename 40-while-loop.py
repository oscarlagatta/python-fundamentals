# while loop; if there is a break the else won't execute.

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')

j = 0
while j < 50:
    print(j)
    break