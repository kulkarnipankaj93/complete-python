# Exceptions are unexpected events that occurs during program execution and it abnormally terminates program execution
# Execution of program terminates mainly because of two things - syntax error or logical exception
# errors are beyond control of programmer we do not try to handle errors
# exceptions can be caught and handled by programmer so that program gets executed further
# We use try-except blocks to handle exceptions
# for example - handle zero division error as follows
try:
    a, b = 10, 0
    result = a/b
    print(result)
except:
    print("Divider is Zero")

print("program ends")


# We can have multiple except blocks handling different exceptions as follows
# Specified exceptions are handled by respective Exception blocks
# 'Exception' is superclass which handles all type of exceptions
# We use 'Exception' if we are not sure about type of exception we will be getting
try:
    a, b = 10, 0
    result = a/b
    print(result)
    list1 = []
    print(list1[1])
    print("continue")              # This statement will not get executed as control of program shifted to except block
except ZeroDivisionError as e:
    print(f"Error is {e}")

except IndexError as i:
    print(f"Error is {i}")

except Exception as x:
    print(f"Error is {x}")

print("program ends")
