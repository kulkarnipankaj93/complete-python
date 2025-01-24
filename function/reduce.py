# we need to import reduce() function from functools module in python
# it applies function to two arguments cumulatively to the items of an iterable
# reduces iterable to single value
from functools import reduce

list1 = list(range(1, 11))


def addition(x, y):
    print(x, y)
    return x+y


result = reduce(addition, list1)           # 1,2,3,4
print(result)
result1 = reduce(lambda x, y: x+y, list1)
print(result1)
