# Applies basic in-build functions to dictionary
fruit1 = {'name': 'Apple', 'colour': 'Red', 'value': 100}
fruit2 = dict({'name': 'Banana', 'colour': 'Yellow', 'value': 50})
fruit3 = dict({'colour': 'orange', 'name': 'orange', 'value': 80})

# Item() function: It provides list having tuples as elements where as each tuple has keys and value as elements
print("Item(): provides list og tuple as elements- ", fruit1.items())

# Keys() function: It provides list of keys present in dictionary
print("keys():provides list of keys present in dictionary- ", fruit1.keys())

# values() function: It provides list of values present in dictionary
print("values():provides list of values present in dictionary- ", fruit1.values())

# Ways to copy one dictionary in to another variable
# 1st way: By using assignment operator
#       : It does not create new memory location, just assign another name to same location
#       : If any changes made to original dictionary it changes new dictionary as well
dict1 = fruit1
print("Original dictionary- ", fruit1)
print("Dictionary with new name- ", dict1)
print("Memory location of dictionary fruit1- ", hex(id(fruit1)))
print("Memory location of dictionary dict1- ", hex(id(dict1)))     # Same memory location

# 2nd way: By using copy function
#       :It creates new memory location
#       :If any changes made to original dictionary it does not changes new dictionary
dict2 = fruit2.copy()
print("Original dictionary- ", fruit2)
print("Dictionary with new name- ", dict2)
print("Memory location of dictionary fruit2- ", hex(id(fruit2)))
print("Memory location of dictionary dict2- ", hex(id(dict2)))

# fromkeys(): It creates new dictionary using sequence
#          : If value is not provided it sets None by default
#          :If value is provided as a sequence then it assign the whole sequence to each key
x = [1, 2, 3, 4]
y = 10
dict3 = dict.fromkeys(x,y)
print("fromkeys():creating new dictionary using:", dict3)

# get(): It returns value for given key
#     : If the key is not present in dictionary then it will return value as None unlike access method
val1=fruit1.get('colour')
print("get():returns value for given key", val1)


# pop() function: It removes given item from dictionary
#              : argument is required if not provided it will give 'TypeError'
print("pop():It removes given item from dictionary", fruit2.pop('colour'))
print(fruit2)


# popitem(): It removes last item from dictionary
fruit3.popitem()
print("popitem():It removes last item from dictionary", fruit3)

# clear(): It removes all the items from dictionary
#       : the structure remains as it is(memory remains allocated)
fruit3.clear()
print("clear(): removes all items from dictionary", fruit3)