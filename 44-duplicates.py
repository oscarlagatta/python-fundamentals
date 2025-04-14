# Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for vaule in some_list:
    if some_list.count(vaule) > 1 and vaule not in duplicates:
        duplicates.append(vaule)

