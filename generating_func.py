def some_gen(begin, end, func):
    count = 0
    value = begin
    while count < end:
        yield value
        value = func(value)
        count += 1

def pow(x):
    return x ** 2

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')