# string indexes
# stored in memory as an ordered sequence of characters
selfish = '01234567'

# [index]
print(selfish[0])


# Slicing
# [start:stop]
print(selfish[0:5])

# [start:stop:stepover]
print(selfish[0:5:2])


print(selfish[1:])

print(selfish[:5])

print(selfish[::1])

print(selfish[-1])

# reverse
print(selfish[::-1])

# Output
# ======
# 0
# 01234
# 024
# 1234567
# 01234
# 01234567
# 7
# 76543210
