# Applying basic functions to tuple
# Declaration
tuple1 = (1, 2, 3, 2, 4, 5, 4, 5)
print(tuple1)

# Tuple functions
print("Following are the functions used in tuple")

# Len(): length function gives the length of tuple
print("len(): Length of tuple is-", len(tuple1))

# Count(): count function counts how many times given element is repeated in tuple
print("count(): Number 4 is repeated-", tuple1.count(4))

# Index(): Index function gives index position of element in tuple
#       : If element is repeated it gives index position for first occurance
#       : If given element is not present in tuple it gives 'ValueError
print("index(): Index position of element 2 in tuple is-", tuple1.index(2))
