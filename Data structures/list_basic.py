# Declaration and basic usage of list
# It accepts all data types
# 1 way to declare
list1 = [1, 2, 11.5, 'a', "accepted"]
print(list1)

# 2 way to declare
list2 = list[(101, 102, 103, 104, 105, 106, 107, 108, 109, 110)]
print(list2)

# Ordered: order of the elements once declared remains same everytime
print(list1)

# Changeable: Elements can be changed anytime
list1[1] = "received"
print(list1)

# Allows duplicate values
list3 = [0, 1, 1, 2, 3, 3, 4, 5, 5]
print(list3)


# Unpacking using string format
str1 = "this is the first element of list {}".format(*list1)
print(str1)

str2 = "The first element is {} and second element is {}".format(*list1)
print(str2)

# Unpacking using arithmetic operators
a, b, c, d, e = list1
print(a, b, c, d, e)

