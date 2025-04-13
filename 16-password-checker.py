
user_name = input('user name ? ')
password = input('password ? ')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{user_name}, your password, '
      f'{hidden_password} is {password_length}'
      f' letters long')