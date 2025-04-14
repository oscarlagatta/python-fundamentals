a = 10
def confusion(b):
    print(b)
    a = 90

confusion(300)



total = 0

def count():
    global total
    total += 1
    return total

print(count())


def count1(total):
    total += 1
    return total

print(count1(count1(count1(total))))

# 1 - start with local scope
# 2 - parent local scope
# 3 - global
# 4 - Built-in Python functions
