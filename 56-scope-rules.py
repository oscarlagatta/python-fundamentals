# a = 1
#
# def confusion():
#     a = 5
#     return a
#
#
# print(a) # 1
# print(confusion()) # 5
#
#
# def parent():
#     a = 10
#     def confusion():
#         return a
#     return confusion()
#
# print(parent())
# print(a)


def parent():
    a = 10
    def confusion():
        return sum
    return confusion()

# 1 - start with local scope
# 2 - parent local scope
# 3 - global
# 4 - Built-in Python functions
