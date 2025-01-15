# Applying basic in-built functions to set
# Declaration
set1 = {'banana', 'apple', 'orange', 'kiwi'}

# len(): gives length of set
print("len(): length of set:", len(set1))

# type(): gives type of variable
print("type(): gives type of variable:", type(set1))

# add: it adds element to the set
set1.add('coconut')
print("add(): adds element:", set1)

# update: it only adds elements to set from given sequence
#      : single element can not be added using this function
# updating set using another set
# We can add tuple as element of set, but we can not add list as element of set if we try it will give 'TypeError'
a = {'papaya', 'lemon'}
set1.update(a)
print("update():set using set:", set1)

# updating set using list/tuple
b = ('mango', 'amla')
set1.update(b)
print("update():set using list/tuple", set1)

# remove: It removes given element from set
#      : only one argument is mandatory if not provided it will give 'TypeError'
#      : If we provide any value as argument which is not present in set it provides 'KeyError'
# set1.remove('abd')
# set1.remove()
set1.remove('lemon')
print("remove(): removes given element:", set1)

# discard: It removes given element from set
#       : Only one argument is mandatory, if not provided gives 'TypeError'
#       : If we provide any value as argument which is not present in set it do not provide any error
set1.discard('abd')
print(set1)

# pop(): It removes single random element from set
#     : it do not accept any argument
val1=set1.pop()
print("pop(): removes single random element:",val1)
print(set1)

# clear(): It removes all elements from set
#       : set memory block remains allocated
set1.clear()
print("clear(): removes all elements:", set1)

# del : it deletes all elements as well as memory block
del set1

