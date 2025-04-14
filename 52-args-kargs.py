# *args **kwargs'

def super_func(*args):
    print(*args)
    return sum(args)



def super_func_kwargs(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items

    return sum(args) + total

print(super_func_kwargs(1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs
