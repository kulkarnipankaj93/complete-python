# It filters elements from iterable based on output of given function
# function is applied to each element and if it returns true then selected by filter function
# It takes to arguments - function and iterable
# it returns an iterator.\
# syntax = filter(function, iterator)
list1 = list(range(1,51))


def even_number(number):
    if number%2 == 0:
        return True
    else:
        return False


result = filter(even_number,list1)
print(list(result))

