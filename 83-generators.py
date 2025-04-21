# # Generators
#
# # We use Range before
# # range(100) # create one by one
# # list(range(100)) # creates the list in memory
#
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
#
# my_list = make_list(100)
# print(my_list)
# #
# #
# #
# # print(list(range(100000)))  # using a lot of memory
#
# # better is to use a generator
#
# # iterable under the hood has the __iter__
# # generators are iterable, not all that is iterable is a generator
# # list is an iterable but not generator
# #
# def generator_function(num):
#     for i in range(num):
#         yield i*2 #  instead of appending to an array we return yield.
#
# for item in generator_function(100):
#     print(item)
# #
# # # what yield does
# #
# # g = generator_function(100)
# # next(g)
# # next(g)
# # print(next(g))
#
# # Under the hood of iterators
# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             item = next(iterator)
#         except StopIteration:
#             break
#         else:
#             yield item
#
#
# class MyGen:
#     current = 0
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration
#
#
# gen = MyGen(0, 100)
# for i in gen:
#     print(i)


# Fibonacci
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a + b

for x in fibonacci(21):
    print(x)

print(list(fibonacci(21)))

# Fibonacci in a list
def fibonacci_list(number):
    result = []
    a, b = 0, 1
    for i in range(number):
        result.append(a)
        a, b = b, a + b

print(fibonacci_list(21))