# Functions
def say_hello():
    print("Hello!")

say_hello()

# parameters
def say_hello_to(name, emoji):
    print(f'Hello, {name} {emoji}')

# positional arguments
say_hello_to("Jane", "emoji")


# keyword arguments; but this is bad practice, should follow
# the original order.
# say_hello_to(emoji="emoji", name="Jane")

# Default parameters
def say_hello_to_with_default(name='Darth Vader', emoji='emoji'):
    print(f'Hello, {name} {emoji}')

say_hello_to_with_default() # I can run and the funciton will use the default parameters
say_hello_to_with_default('Jane')

# def add(x, y):
#     return x + y
# print(add(3, 4))
# def add_two_numbers(x, y):