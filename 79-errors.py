# Error Handling

# Syntax Error
# def hooo()
#     pass

# NameError
# def hoo2():
#     1 + name

# IndexError
# def hoohoo():
#     li = [1,2,3]
#     li[5]

# How do we avoid errors

while True:
    try:
        age = int(input("What is your age? "))
        10 / age
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('you cannot divide by zero')
    else:
        print('thank you')
        break