# Basics of set
# Declaration
set1 = {2, 4, 'ab', 1.5, 'xy'}

# Characteristics
# Unordered- Order of the elements in set does not remain same
# Unchangeable- Elements of set can not be changed but we can add or remove elements from set
# Duplicates- It does not accept duplicate values, if provided it will consider it as a single element
# Unindexed- index values are not provided, so elements can not be accessed using index values
# True=1 and False=0. true is considered as 1 and false as 0.

print(set1)

# Operators
# + this operator does not work on set. It provides 'TypeError'
# * repetation operator does not work on set. It provides 'TypeError'

# in operator- It checks presence of given element in set and returns boolean value
value1 = 'ab'
result1 = value1 in set1
print("in operator- checks presence of element in set:", result1)

# not in operator-
value2 ='xy'
result2 = value2 not in set1
print("not in operator:", result2)

# Accessing elements using for loop
print("for loop:")
for i in set1:
    print(i)

# Accessing elements using while loop
# Elements of set can not be accessed using index that's why pop function is used to access elements using while loop
print("while loop:")
while set1:
    print(set1.pop())

