# Formatted Strings

name = 'Johnny'
age = 55

print('hi ' + name + ',You are ' + str(age)  + ' years old')
print(f'hi {name} You are {age} years old') # way to go
print('hi {} You are {} years old'.format('Johnny', '55'))

print('hi {1} You are {0} years old'.format(age, name))
print('hi {new_name} You are {age} years old'.format(new_name='sally', age=100))
