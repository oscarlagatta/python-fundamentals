li = [1, 2, 3, 4, 5]
li2= ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

# List slicing
print(amazon_cart[0])
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
print(new_cart)
print(amazon_cart)

