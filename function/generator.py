# Used when we want to generate large number of values but not store them in memory at once
# it is used when we temporarily want to take control out of function and return current value
# 'yield' keyword is used which returns current value and takes control out of function
# Example

def get_numbers():

    for i in range(1,11):
        yield i
        print("after function call")


# syntax- (expression for item in iterable)
for x in get_numbers():
    print(x)


def func():
    print("1st statement")
    yield "1st out"
    print("2nd statement")
    yield "2nd out"
    print("3rd statement")
    yield "3rd out"


for j in func():
    print(j)