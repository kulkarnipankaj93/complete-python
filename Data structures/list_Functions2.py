# applying basic in-built functions to list
# Declaration
list1 = list(range(1, 11))
print("List1 is- ", list1)

list2 = [12, 13, 14, 15]

# max,min function: To get highest and lowest value from list
max_number = max(list1)
min_number = min(list1)
print(f"Max number is {max_number}. Min number is {min_number}")

# count: returns number of occurrences of value in list
occurance = list1.count(10)
print("count(): counts occurance of element in list like 10 occurs- ", occurance)

# append: it always adds appended value at the end of list
list1.append(11)
print("append(): adds value at the end of list- ", list1)

# extend: adds second list elements to first list (changes list 1)
list1.extend(list2)
print("extend(): adds iterable to list- ", list1)

# insert: insert given element at given index position
list2.insert(2,'a')
print("insert(): adds value at the given index position in list- ", list2)
# if index position is more than index present in list it adds value at end of list
list2.insert(8,'b')
print("insert(): if index value is more than index present, adds at the end- ", list2)


# pop: removes element at given position
list2.pop(2)
print("pop(): removes element at given index position- ",list2)
# if index position is not defined it removes last element
list2.pop()
print("pop(): if index position is not provided removes last element- ", list2)

# remove(): It removes given element from list
#         : Unlike pop we have to provide value of element to be removed rather than index position
list2.remove(14)
print("remove(): removes given element from list- ", list2)

# reverse: used to reverse the list
list2.reverse()
print("reverse(): reverses and update the list", list2)

# sort(); sort list in asc/desc order
# for ascending order
list2.sort()
print("sort(): sort list in ascending values- ", list2)

# for descending order
list2.sort(reverse=True)
print(list2)

# clear: removes all elements from list but the structure remains
list2.clear()
print("clear(): removes all elements but keeps structure at it is- ", list2)

# del: Deletes the list from memory
del list2
# print(list2)  # It will give error as list2 is not present at all

