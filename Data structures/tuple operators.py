# How operators works on tuple
# Declaring tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
print("Given tuples are-", tuple1, tuple2)

# Unpacking tuple using *- * operator unpacks tuple into list if used with variable even with less variables used
a, *b, c = tuple1
print("Unpacked tuple using * is-", a, b, c)

# Unpacking-one to one mapping is done when we unpack tuple using different variables
#         -if we use less number of variables than elements it gives 'ValueError'
m, n, o, p, q = tuple1
print(m, n, o, p, q)

# + operator- it adds two tuples and returns single tuple
tuple3 = tuple1 + tuple2
print("+ operator: Adds two tuples as-", tuple3)

# * operator- it repeats tuple for given number of times
print("* operator: it repeats tuple for given number as-", tuple1*3)

# == operator- it compares two tuples element by element and returns boolean value as result
print("== Operator compares two tuples and returns boolean value as-", tuple1 == tuple2)

# != operator-
print("!= operator returns true if tuples are not equal as-", tuple1 != tuple2)

# in operator- checks if given element is present in tuple or not and returns boolean value
print("in operator checks for given element in tuple and returns boolean value as-", 10 in tuple2)

# not in operator- returns true if given element is not present in tuple
print("not in returns true if given element is not present in tuple as- ", 101 not in tuple1)
