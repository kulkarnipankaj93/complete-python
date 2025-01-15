# Basics of String
# Declaring
# 1 way- using ""
str1 = "Basics of Python programming language"
str2 = "python"

# 2 way- using ''
str3 = "programming"

# 3 way- Multiline string using """ """
str4 = """This is
        Multiline
        String declared"""

# Printing strings
print("Declared strings are")
print("String 1-", str1)
print("String 2-", str2)
print("String 3-", str3)
print("Multiline string is-", str4)

# Rules
# 1- String is Immutable- It creates same memory block for two variables having same string
#                      - Elements of the string can not be changed, replaced or add
# 2- We can access elements of string using positive as well as negative indexing
# 3- Spaces are counted in index values


# Accessing- We use index values to access the elements
#         - if the index value exceeds present index we get 'IndexError'
val1 = str1[10]
val2 = str1[-8]
print("Accessing string element using positive index-", val1)
print("Accessing string element using Negative index-", val2)

val3 = str1[6]
print("Accessing space element in string-", val3)

# Slicing
val4 = str1[:16]
print("Slicing the string-", val4)

val5 = str1[17:]
print("Slicing the string-", val5)

val6 = str1[0::2]
print("Slicing the string using step-", val6)

# Program to reverse string using slicing
rev1 = str2[::-1]
print("Reversed string using slicing-", rev1)

# len() function
length = len(str1)
print(length)

