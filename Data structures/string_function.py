# Applying in-built functions on string
# Declaration
str1 = "Welcome to the new world of Computer Programming"
str2 = "Basics of Python programming language"
str3 = "python"
str4 = "123 456"

# Upper case- It converts string to upper case and returns new string
#          - upper function do not take any argument, if given it gives 'TypeError'
print("upper(): converts string to upper case as-", str2.upper())

# Lower case- It converts string to lower case and returns new string
#          - lower function do not take any argument, if given it gives 'TypeError'
print("lower(): converts string to lower case as-", str2.lower())

# len() function- It calculates the length of string
#              - It also calculates the spaces
print("len(): calculate Length of string-", len(str1))

# count() function- It returns the number for which a given character occurs in string
#                - If the character is not present in string it returns value 0
print("count(): calculate occurance of Character in string for 'o'-", str1.count("o"))

# endswith function - Returns value True if string ends with given value
#                 - Always returns boolean value
print("endswith(): checks ending of string for given value-suppose 'language'-", str2.endswith("language"))

# startswith function- Returns value True if string starts with given value
print("startswith(): checks starting of string for given value-suppose 'check'-", str1.startswith("check"))

# find function- It returns starting index value of given substring in main string if found
#             - If the given substring is not present in main string it returns value -1
#             - If the given substring is present multiple times it returns index value for first occurance
#             - Correct function to use when not sure about presence of substring in main string
print("find(): Returns starting index value of given substring- suppose 'the'-", str1.find("the"))

# index function- It returns starting index value of given substring in main string if found
#              - If the given substring is not present in main string it gives 'ValueError'
#              - If the given substring is present multiple times it returns index value for first occurance
#              - Not a Correct function to use when not sure about presence of substring in main string
print("index(): Returns index value of given substring- suppose 'n'-", str1.index("n"))

# isalnum()- Returns true if the string is alpha-numeric
print("isalnum(): Returns true if the string is alpha-numeric-", str1.isalnum())

# isalpha()- Returns true if all characters in string are alphabets
#         - Do not consider space as alphabet, so if there is space in string it will return false
print("isalpha(): Returns true if all the characters in string are alphabets-", str2.isalpha())

# isdigit()- Returns true if all characters are digit
#         -Do not consider space as digit,so if there is space in string it will return false
print("isdigit(): Returns true if all characters are digit-", str1.isdigit())

# split()- It divides string based on given character and returns list of strings
#       - It do not consider the given character
print("split(): Divides string based on given character and returns list of string- suppose 'o'", str1.split("o"))
