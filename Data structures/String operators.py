# How operators work on string
str1 = "Basics of Python programming language"
str2 = "python"
str3 = "programming"

# +: concatination- It concats two strings
#                - Need to add space if we want to differentiate two strings
re1 = str2+str3
print("+ operator concats two strings as-", re1)
r1 = str2 + " " + str3
print("+ operator after adding space-", r1)

# *: repetation- It repeats string for given number of times
r2 = str2 * 3
print("* Operator repeats string as-", r2)

# in: membership operator- It checks presence of sub string into main string and returns boolean value
r3 = "language"
print("checking presence of string 'language' in main string using in operator-", r3 in str1)

r4 = "java"
print("checking presence of string 'java' in main string using in operator-", r4 in str1)

# Comparison operators- It compares two strings element by element and returs boolean value
print("== operator Comparing two strings-", str2 == str3)

# Need to study more on this
print(str1 > str3)

