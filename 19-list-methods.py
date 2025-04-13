# Python List/Array methods

basket = [1,2,3,4,5]
# adding

# new_list = basket.append(100)

print(basket)
new_list = basket
print(new_list)
print(len(basket))

# insert
basket.insert(4, 100) # inserts but doesn't create a new copy of the list
print(basket)

basket.extend([100, 101])
print(basket)

#remove
basket.pop()
print(basket)
basket.pop(0)
print(basket)

basket.remove(4)
print(basket)

# new_list = basket.pop(4)
# print(new_list)

basket.clear()
print(basket)

# Methods 2
basket = ['x','a','b','c','d','e','d']
print(basket.index('d', 0, 5))
print('d' in basket)
print('x' in basket)
print('i' in 'hi my name is Ian')
print(basket.count('d'))

# Methods 3
# basket.sort()
# sorted(basket)
print(f'Sorted {sorted(basket)}')
print(f'basket {basket}')
new_basket = basket.copy()
basket.sort()
basket.reverse()
print(f'Sort and Reverse {basket}')

# Methods 4

print(f'basket after  basket[::-1] {basket}')
print(basket[::-1]) # +. reverse again and creates a new list
print(f'basket[::-1] {basket[::-1]}')

print(list(range(100))) # Generates a list

# join works on strings
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])

print(new_sentence) # hi my name is JOJO



