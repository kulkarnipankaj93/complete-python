# statements which allows program to test several conditions and execute instructions based on which condition is true
# if statements: runs code when only given condition is satisfied
# for example:
n = 10
if n % 2 == 0:
    print("n is an even number")

l = []
# when we use variable in place of condition it returns false if variable is= empty, false,None,0
# returns true if variable has some value
if l:
    print(l)

# if-else:
# for example:
list1 = [1, 2, 3, 4, 5]
for i in list1:
    if i % 2 == 0:
        print(f"{i} is odd")
    else:
        print(f"{i} is even")

# if-elif-else statement: we use this if the choice is between more than two alternatives
# for example:
a = 10
b = 12
c = 20

if a > b:
    if a > c:
        print("a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")

# Nested if statement: if statement inside another if statement

