# Logical Operators

# >
# <
# ==

print (4 > 5)
print (4 < 5)
print(4 == 5)
print('a > b')
print('a' > 'b')
"""
- `'a'` has a Unicode code point of `97` (lowercase 'a').
- `'b'` has a Unicode code point of `98` (lowercase 'b').

When comparing `'a' > 'b'`:
- Python checks the Unicode value of `'a'` (`97`) and compares it with the Unicode value of `'b'` (`98`).
- Since `97` is **not greater than** `98`, the result is `False`.

"""
print('a > A')
print('a' > 'A')

print( 1 < 2 >  3 < 4)

print(1 <= 0)
print(0 != 0)

print(not(True))
