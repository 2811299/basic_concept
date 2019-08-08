dict = {'a': 'b', 'c': 'd'}
dict.popitem()
print(dict)


def test():
    for i in range(1, 10):
        yield i


r = test()
import types

print(isinstance(range(10), types.GeneratorType))

print('ga')

for i in r:
    print (i)

print(range(10))
print((i for i in range(10)))
def multi():
    return [lambda x : i*x for i in range(4)]
print([m(3) for m in multi()])

print(filter(lambda x: x % 2 == 0, range(10)))