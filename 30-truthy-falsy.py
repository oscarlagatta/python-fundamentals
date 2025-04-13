# # Conditional Logic

# is_old = 'hello'
# is_licenced = bool(5) # conversion

# User
password = '123'
username = 'Oscar'

if password and username:
    print('you have password and user name')


# Truthy and Falsy

# Truthy
print(bool('hello')) # True
print(bool(5)) # True

# Falsy
print(bool('')) # False
print(bool(0)) # False
print(bool(None))


# All values are considered truthy except for the following which are falsy
# -------------------------------------------------------------------------
# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0,1)
# [] empty list
# [] empty dict
# () empty tuple
# '' empty str
# b'' an emtpy bytes
# set() an emtpy set
# an empty range, line range(0)
# objects for which
    # ojb.__bool__() returns False
    # obj.__len__() returns 0




if is_old and is_licenced:
    print('you are old enough to drive and you have a license')
# elif is_licenced:
#     print('you can drive now')
else:
    print('you are not of age!')

print('okokok')