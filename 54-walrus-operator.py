# walrus operator :=
a = 'hellooooooooooo'

if len(a) > 10:
    print(f'Too long: {len(a)} elements')

if ((n := len(a)) > 10):
    print(f'Too long: {n} elements')

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

