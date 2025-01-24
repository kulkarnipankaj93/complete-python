# we can import module as given below
# when we import any module it gets executed first and check if there is any error in imported file
# it prints statements from imported file first if any then executes current module
import basics as b                     # Aliasing basics as b

# to list down all functions and constants from imported module we use
print(dir(b))

# to use different functions present in imported module
r1 = b.addition(10, 20)
print(r1)

r2 = b.sub(50, 10)
print(r2)

r3 = b.mul(10, 20)
print(r3)
