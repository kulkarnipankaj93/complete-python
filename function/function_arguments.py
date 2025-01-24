# arguments - we can provide multiple arguments to the function.
# Types of arguments are-
# 1- positional argument - provides one to one mapping of arguments passed
# 2- default argument - default value is already provided. if no value is passed while calling it will use default value
# 3- keyword argument - values to argument is provided by using assignment operator.
# 4- variable number of positional arguments - used when we are not sure about number of arguments.
# 5- variable number of keywords arguments - used when we pass key and values but not sure about number.


# Example for positional argument
def addition(x, y):
    print(x, y)
    return x+y


a = 10
b = 20
result1 = addition(a, b)
print(result1)


# Example for default argument
def message(name,course_name="python"):
    print(f"Hello {name}, welcome to {course_name}")


message("Akshay","python")
message("pankaj")                               # Here it uses default value as python
message("laxman","devops")


# Example for keyword argument
def student(name,roll_num):
    print(f"name of student is {name} and ID is {roll_num}")


student(roll_num=23, name="pankaj")


# Combination of positional and keyword - positional argument followed by keyword argument
# student(15,name="Rahul")

# Example for variable number of positional argument -
# This is used when we are not sure about number of arguments we are going to provide
# * is used before argument and it will convert multiple variables into list or tuple
# we can provide any number of values or no values
def cal_square(*args):
    print(args)
    for i in args:
        print(i*i)


a = [5, 6, 7]
cal_square(1, 2, 3, 4)
cal_square(*a)


# Variable number keyword arguments -
# Used when we pass key and values to arguments but not sure about its number.
# ** is used before argument and it will convert variables into dictionary.
# we can provide any number of values or no values.

def obj_color(**kwarg):
    print(kwarg)
    for key, value in kwarg.items():
        print(key, value)


b = {"rose": "red", "sky": "blue"}
obj_color(**b)
