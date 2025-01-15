# Basic functioning of dictionary
# Declaration
# 1 way
fruit1 = {'name': 'Apple', 'colour': 'Red', 'value': 100, 'quantity': None}
# 2 way
fruit2 = dict({'name': 'Banana', 'colour': 'Yellow', 'value': 50})
fruit3 = dict({'colour': 'orange', 'name': 'orange', 'value': 80})

# Printing dictionary
print(fruit1)
print(fruit3)

# Rules
# Order of the keys and values always remains same
# Changeable - Both values and the keys can be changed in the dictionary
# Duplicate- It do not allow duplicate keys,if provided second value will overwrite first one.
#            Duplicate values can be provided

# finding type of function
print("Type of fruit1 variable is- ", type(fruit1))

# finding length of dictionary
print("Length of dictionary fruit1 is- ", len(fruit1))

# Accessing values of dictionary - key name can be used along with dictionary name to access values of dictionary
#                              - If we provide any key which is not present it will raise 'KeyError'
print(f"Fruit {fruit1['name']} has colour {fruit1['colour']} and price {fruit1['value']}.")

# Updating value
fruit2['name'] = 'Mango'
print("Updating values-", fruit2)

# Adding new keys and values to dictionary
# 1 way
fruit1['quantity'] = 3
print("Adding keys and values:", fruit1)

# 2 way - using update function- used to add as well as update dictionary
fruit2.update({'value': 70, 'quantity': 5})
print("update(): add and update dictionary:", fruit2)

# Accessing dictionary using for loop
# 1 way: Using item function and two variables
for i, j in fruit1.items():
    print(f"key {i} has value {j}")

# 2 way: Using single variable
for i in fruit2:
    print(f"value {fruit2[i]} associated with key {i}")

# 3 way: Using one variable and item function
#     : It provides separate tuples for key and value
for i in fruit3.items():
    print(i)

