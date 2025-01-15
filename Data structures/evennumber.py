# #Declaring list using range
# req_range = list(range(1,51))
# list1 = []
# print(req_range)
#
# for i in req_range:
#     list1.append(i)
#
# print(list1)
#
# #Printing even numbers using for loop
# for a in list1:
#     if(a%2==0):
#         print(a)
#
# #Printing even numbers using while loop
# x=0
# y=len(list1)
# while(x<=y):
#     if (x%2 == 0):
#         print(x)
#     x=x+1


# #Declaring tuple using range
# tuple1 = tuple(range(1,51))
#
#
# print(tuple1)

# for i in tuple1:
#     if(i%3==0):
#         print(i)

# x=0
# y=len(tuple1)
#
# while(x<y):
#     if(tuple1[x]%3==0):
#         print(tuple1[x])
#     x=x+1

# range1 = range(1,51)
# list1 = list(range1)
# print(list1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)

# for i in list1:
#     rem=i%2
#     if(rem==0):
#         print(i)

a=0
while a < len(list1):
    if list1[a]%2 == 0:
        print(list1[a])
    a = a+1

