# Error Handling

while True:
    try:
        age = int(input("What is your age? "))
        10 / age
        raise ValueError('Hey cut it out')
    # except ValueError:
    #     print('please enter a number')
    #     continue
    except ZeroDivisionError:
        print('you cannot divide by zero')
        break
    else:
        print('thank you')
    finally:
        print('ok, I am finally done')
        print('this will always run')
    print('can you hear me ?')