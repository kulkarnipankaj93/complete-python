# Here we provide one function as an argument to another function
# For example
def lower_case(str1):
    return str.lower(str1)


def upper_case(str1):
    return str.upper(str1)


def given_str(fun_name):
    result = fun_name("Welcome to Python")
    return result


r1 = given_str(upper_case)
print(r1)