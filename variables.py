# Variables
# =========
# name = assignment
iq = 190
print(iq)

# snake_case
# start with lowercase or underscore
# letters, numbers, underscores
# Case sensitive
# Don't overwrite keywords

user_iq = 190
print(user_iq)

# _ signifies private variable
_user_iq = 190
print(_user_iq)

user_age = iq / 4
print(user_age)

a = user_age
print(a)

# GOTCHAS

# Constants
PI = 3.14

# We should not create variables with two underscores __
__user_iq = 190

# Short-hand
a,b,c = 1,2,3

print(a)
print(b)
print(c)
