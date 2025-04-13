# Exercise Logical Operator

is_magician = True
is_expert = False

# Check if magician and expert "you are a master magician"
# check if magician but not expert "at least you're getting there"
# if you are not a magician "you need magic powers"
if is_magician and is_expert:
    print('you are a master magician')

elif is_magician and not is_expert:
    print('you are getting there')

elif not is_magician:
    print('you need magic powers')
