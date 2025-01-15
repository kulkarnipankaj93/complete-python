# Logical operators and operations on them
num1 = True
num2 = False
num3 = True

# And operator
# (T and T)
result1 = num1 and num3
print("True and True- ", result1)

# (T and F)
result2 = num1 and num2
print("True and False- ", result2)

# (F and F)
result3 = num2 and False
print("False and False- ", result3)

# Or operator
# (T or T)
result4 = num1 or num3
print("True or True- ", result4)

# (T or F)
result5 = num1 or num2
print("True of False- ", result5)

# (F or F)
result6 = num2 or False
print("False or False", result6)

# Not operator
print("not True = ", not num1)
print("not False = ", not num2)

