# comprehensions are concise and expressive ways to create list, dictionaries and sets.
# they provide compact syntax.
# tuple comprhensions are not supported by python


# List Comprehensions- concise way to create list comprise of for loop and conditional statement
# for example- create list of squares of even numbers from 1 to 10
# Traditional way-

# sq1=[]
# for i in range(1,11):
#     if i%2==0:
#         sq1.append(i**2)
#
# print(sq1)

# List comprehension way-
# syntax= processing block i, for statement,condition(optional)
sq2=[i**2 for i in range(1,11) if i%2==0]
print(sq2)


#Set comprehensions- similar to list comprehension only difference is of brackets
#for example- create set of squares of odd numbers from 1 to 10
#Traditional way
# set1=set ()
# for i in range(1,11):
#     if i%2!=0:
#         set1.add(i**2)
#
# print(set1)

#comprehension-
set2={i**2 for i in range(1,11) if i%2!=0}
print(set2)


#Dictionary comprehension-
#for example- create dictionary of squares of numbers greater than 5 and less than 10
#Traditional way-
# dict1={}
# for x in range(1,11):
#     if x>5:
#         dict1[x]=x**2
#
# print(dict1)

#Comprehension-
dict2={x:x**2 for x in range(1,11) if x>5}
print(dict2)