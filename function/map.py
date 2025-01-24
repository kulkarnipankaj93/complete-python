# map function applies to given function to each element of iterable and returns iterator containing result.
# It takes two arguments- a function and iterable like list,set etc.
# syntax- map(function, iterable)
# no other argument than iterable can be passed
# 1st Example

a = list(range(0, 11))


def square(x):
    return x*x


result1 = map(square, a)
y = list(result1)
print(y)

# 2nd Example

list2 = [1, 2, 3, 4, 5]
list3 = [6, 7, 8, 9]


def addition(x,y):
    return x+y


result2 = map(addition, list2, list3)
z = list(result2)
print(z)

# Program to perform addition of two numbers in tuple as element of list
list1 = [(1, 2), (2, 3), (3, 4), (4, 5)]


def add(x):
    print(x)
    return x[0]+x[1]


result3 = map(add, list1)
print(list(result3))
