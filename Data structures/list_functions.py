# Applying basic in-built functions to list
list1 = [101, 102, 103, 104, 105, 106, 107]
print(list1)

# Positive Indexing
print("Accessing list element using positive indexing", list1[4])

# Negative Indexing
print("Accessing list element using negative indexing", list1[-4])

# Print list using for loop
print("Printing list using for loop")
for i in list1:
    print(i)

# Print list using while loop
print("Printing list using while loop")
counter = 0
while counter < len(list1):
    print(list1[counter])
    counter = counter+1

# len() function- to calculate length of list
r1 = len(list1)
print("len(): length of list- ", r1)

# type() function- to get the type
print("type(): type of list1", type(list1))

# Slicing function-positive
# var[start:stop:end]
print(list1[0:7:1])    # start=0 =101
                       # 0+1 = 1   = 102
                       # 1+1 = 2   = 103

print(list1[2:6:2])    # start=2  =103
                       # 2+2=4    =105
                       # 4+2=6

# Slicing function- Negative
print(list1[-1:-7:1])   # start=-1
                        # -1+1=0

print(list1[-1:-8:-2])  # start=-1 =107
                        #-1-1=-2  =106
                        # -2-1     = 105

print(list1[-4::1])     # start=-4 =104
                        #-4+1=-3  =105
                        #-3+1=-2  =106
                        #-2+1=-1  =107


#Reverse list using slicing
list1_reversed = list1 [::-2]
print(list1_reversed)


