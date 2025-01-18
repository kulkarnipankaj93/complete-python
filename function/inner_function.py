# When we have function inside function called as Inner function or Nested function.
# Scope of inner function is only with in outer function.
# This function we mainly use for initializing login credentials.
# For Example
def outer_function():
    print("Inside outer function")

    def inner_function():
        print("Inside inner function")


    inner_function()


outer_function()

# -------------------------------------------------------------
# Returning inner function reference - here we can also return a function reference as a return value


def welcome(name):
    def message():
        return f"Welcome to python {name}"
    return message                          # No parenthesis after message


result1 = welcome("pankaj")
print(result1)                              # prints function reference
print(result1())                            # prints function value


# --------------------------------------------------------------------------
# Returning inner function call - returns function call as a return value


def new_student(roll_num):
    def info():
        return f"Your roll number is {roll_num}"
    return info()                               # parenthesis after function


result2 = new_student(23)
print(result2)