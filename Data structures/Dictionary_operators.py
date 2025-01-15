# Performs how dictionary performs with operators
fruit1 = {'name': 'Apple', 'colour': 'Red', 'value': 100}
fruit2 = dict({'name': 'Banana', 'colour': 'Yellow', 'value': 50})
print("fruit1 -", fruit1)
print("fruit2 -", fruit2)

# + and * operators are not supported by dictionary. it gives 'TypeError'

# in operator- It checks present of key and values in given dictionary
#           - It always returns boolean value
# checking key in dictionary
key1 = 'value'

r1 = key1 in fruit1
print("value key is present in fruit1- ", r1)

# checking value in dictionary
val1 = 'Red'
r2 = val1 in fruit1.values()
print("Red value is present in fruit1- ", r2)

# not in operator-
key2 = 'quantity'
r3 = key2 not in fruit1
print("quantity key is not present in fruit1- ", r3)

