# Applying basic in-built functions to set
# Declaration
car_models = {'Nexon', 'Nano', 'Ecosport', 'Creta', 'Freestyle', 'Seltos', 'Figo'}
tata_models = {'Nexon', 'Nano', 'Indica', 'Harrier', 'Tiago'}
ford_models = {'Ecosport', 'Freestyle', 'Figo'}
audi_models = {'A6'}

# difference: returns set containing items that exist only in the first set, and not in both sets.
#          : If argument is not provided it do not give any error

# using  function
set1 = car_models.difference(tata_models)
# using operator
# set1=car_models-tata_models
print(set1)

# difference_update: It updates original set by eliminating common elements
# car_models.difference_update(tata_models) - using function
# car_models-=tata_models  - using operator
# print(car_models)

# intersection: It returns set of common elements
#            : If no common elements then it returns empty set
#            : If no argument is provided it returns all the values from first set
set2 = car_models.intersection(tata_models)    # Using function
# set2 = car_models&tata_models                 # using operator
print(set2)

# intersection_update: It updates original set by using common elements only
# car_models.intersection_update(tata_models)   #using function
# car_models&=tata_models                       #Using operator
# print(car_models)

# isdisjoint: It returns True if there is no common element between two sets
#          : If any common element present it returns false
result1 = car_models.isdisjoint(audi_models)
print(result1)

# issubset: Returns true if all the elements of given set are present in required set
result2 = ford_models.issubset(car_models)        # using function
# result2 = ford_models<=car_models                 # using operator
print(result2)


# Example- to check subset
# list1=[10, 20, 30, 40, 50, 60]
# dict1={1:10, 2:20, 3:30, 4:40}
# s1 = set(list1)
# s2 = set(dict1.values())
# r1 = s2.issubset(s1)
# print(r1)

# issuperset:Returns true if given set is super set
result3 = car_models.issuperset(ford_models)   # Using function
# result3 = car_models >= ford_models             # Using operator
print(result3)

# symmetric_difference: returns set containing a mix of items that are not present in both sets.
set3 = car_models.symmetric_difference(tata_models)    # Using function
# set3 = car_models^tata_models                         # Using operator
print(set3)


# symmentric_difference_update: It removes common elements and update original set by adding remaining elements
# car_models.symmetric_difference_update(tata_models)    #Using function
# car_models^=tata_models                               #Using operator
# print(car_models)

# union: It returns set containing all the elements from both the set
set4 = car_models.union(tata_models)
print(set4)

