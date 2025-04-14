# Functions Return
# def sum(num1, num2):
#     return num1 + num2 # return is used to return the result.
#     # if we don't provide a return then will return None.
#
# print(sum(4, 5))
#
# total = sum(4, 5)
# print(total)
#
# print(sum(10, sum(10,5)))

def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total2 = sum2(4, 5)
print(total2)