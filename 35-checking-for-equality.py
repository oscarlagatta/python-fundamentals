# Checking for equality

print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == [])  # True

# Double equals check for equality of value. First case conversion happens of bool(1) which is Truthy
# Empty string is falsy so False is not equal to Truthy
# Empty Array is falsy so False is not equal to Truthy


# is checks if the location in memeory is the same

print('1' is '1') # True
print([] is []) # False (locations in memory are different) different lists
print(10 is 10) # True
a = [1,2,3]
b =  [1,2,3]
print(a is b)  # False
print(a == b) # True
