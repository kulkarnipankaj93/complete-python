# applying basic in-built functions to list
# Declaration
list1 = list(range(1, 11))
print(list1)

list2 = [12, 13, 14, 15]

# max,min function: To get highest and lowest value from list
max_number = max(list1)
min_number = min(list1)
print(f"Max number is {max_number}. Min number is {min_number}")

# count: returns number of occurrences of value in list
occurance = list1.count(10)
print(occurance)

# append: it always adds appended value at the end of list
list1.append(11)
print(list1)

# extend: adds second list elements to first list (changes list 1)
list1.extend(list2)
print(list1)

# insert: insert given element at given index position
list2.insert(2,'a')
print(list2)
# if index position is more than index present in list it adds value at end of list
list2.insert(8,'b')
print(list2)


# pop: removes element at given position
list2.pop(2)
print(list2)
# if index position is not defined it removes last element
list2.pop()
print(list2)

# reverse: used to reverse the list
list2.reverse()
print(list2)

# sort(); sort list in asc/desc order
# for ascending order
list2.sort()
print(list2)

# for descending order
list2.sort(reverse=True)
print(list2)

# clear: removes all elements from list but the structure remains
list2.clear()
print(list2)

# del: Deletes the list from memory
del list2
print(list2)