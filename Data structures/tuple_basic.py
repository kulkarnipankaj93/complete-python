# Declaration
# 1 way
tuple1 = (1, 2, 3, 2, 4, 5, 4, 5)

# 2 way
tuple2 = tuple([11, 'a', "hello", 6.7])

# 3 way
tuple3 = 101, 102, 103, 104, 105, 106

# Characteristics of tuple
print("Following are characteristics of tuple")
# Duplicate: It accepts duplicate values
print("Tuple accepting duplicate values:", tuple1)

# Order: Order of the tuple always remains same
print("same order for tuple:", tuple1)

# Immutable: tuple is immutable
print("Tuple is Immutable: Elements of tuple can not be changed")

# Operations on tuple
print("we can perform following operations on tuple")

# Accessing: We can access particular element of tuple using index
print("Accessing value at index 3:", tuple1[3])

# Slicing: part of tuple can be taken out using index positions
print("Slicing tuple from 3 to 6 index position as:", tuple1[3:7])
#       : Reversing tuple using slicing
print("Reversed tuple using slicing is-", tuple1[::-1])

# Traversing through tuple

# Using for loop
print("Traversing through tuple using for loop:")
for i in tuple1:
    print(i)

# Using while loop
print("Traversing through tuple using while loop:")
index = 0
while index<len(tuple1):
    print(tuple1[index])
    index = index+1
