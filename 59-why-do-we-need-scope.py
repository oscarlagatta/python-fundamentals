# Scope - what variables do I have access to ?

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner', x)
    inner()
    print('outer', x)

outer()
