# Nested List = List inside list
list1 = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
print("Nested list is-", list1)

# Accessing nested list using its index
print("Nested list with known index-", list1[5])

# Accessing nested list element using index position
print("Nested list Element using index position-", list1[5][2])

# Accessing nested list with unknown index position
print("Accessing nested list with unknown index position:")
for i in list1:
    print(i)
    if type(i) == list:
        for j in i:
            print(j)

# Nested tuple and list:
tuple1 = (1, 3.4, 'd', [1, 2, 3, 4, 5, [11]], ('a', (), 'b', 'c'))
print("Nested tuple and list is-", tuple1)

# Accessing nested list element inside tuple
print("Nested list element inside tuple-", tuple1[3][5][0])

# Accessing nested list and tuple with unknown index position:
print("Accessing nested list and tuple with unknown index positions")

for i in tuple1:
    print(i)
    if type(i) == list:
        for j in i:
            print(j)
    if type(i) == tuple:
        for j in i:
            print(j)
