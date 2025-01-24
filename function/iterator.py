# we use iter() and next() functions
# it is set of methods that enables an object to be used in for loop
# every time we use next statement it uses next element in the sequence
# if we use next statement more than the elements present in sequence it will throw StopIteration error
# for example:
list1=list(range(11))
iter1=iter(list1)
print(type(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))



