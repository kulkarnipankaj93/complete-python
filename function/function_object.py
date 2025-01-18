# Instead of directly calling function we create object of function and call the function using object
# This method is used to call function when we want to hide actual signature of function
def square(x):
    return x**2


var1 = square
r1 = var1(10)
print(r1)