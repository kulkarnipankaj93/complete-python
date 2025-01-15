# List and how it works with different operators
# Declaration
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [1, 5, 2, 4, 3]

# +: combines two lists
list4 = list1 + list2
print("List after + operator- ", list4)

# *: repetation
print("List after repetation operator", list1*4)

# in: checks member in list
num = 51
result1 = num in list1
print("51 element is in list1- ", result1)

# not in:
num1 = 1
result2 = num1 not in list1
print("1 element is not in list1", result2)

# ==: compares lists: It compares values of elements of list in sequence
result2 = (list1 == list2)
print("List1 is equal to list2- ", result2)

result3 = (list1 == list3)
print("list1 is equal to list3- ", result3)

# !=: not equal to:
result3 = (list1 != list2)
print("list1 is not equal to list2- ", result3)

