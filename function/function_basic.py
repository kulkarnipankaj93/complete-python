# function- self contained block of codes that encapsulates a specific task or group of tasks.
# program - write down program to find out given number is even or odd using function

# benefits of using function-
# 1- code Reusable - we can use same function multiple times in our program
# 2- code Readability- functions breaks code into chunks which makes program readable and reusable

# Types of functions-
# 1- standard library functions - these are builtin functions in python
# 2- user-defined functions - we can create our own functions

# Parts of function definition-def keyword, function name, arguments, return statement
# def keyword- it defines function.
# function name - user can provide any function name, but it must specify the task it performs like addition()
# arguments- we can provide multiple arguments to the function.
#          - Types of arguments are positional argument, default argument, keyword argument,
#          - variable number of positional arguments, variable number of keywords arguments
# return statement- function can return multiple values separated by commas. it can return any value or sequence.
#                 - while returning any value we need to capture it.
#                 - multiple variables are required to capture multiple return values they provide one to one mapping
#                 - we get 'ValueError' if less number of variables are provided to capture return values


def addition(a,b):                     # function definition
    print("Given numbers are-",a,b)    # function body
    return a+b                         # return statement


result1 = addition(10,20)        # function calling and capturing return value
print("addition result is-", result1)

