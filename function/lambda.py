# It is special type of function without function name
# 'lambda' keyword is used instead of 'def' keyword
# syntax- lambda arguments : expression
# lambda function is used for simple expressions where no complex structures are present like for loop etc.

# 1st example
greet = lambda name : print("hello", name)
greet("pankaj")

# 2nd example- calculate square
square = lambda x:x*x
result = square(2)
print(result)

# 3rd example- data sorting
data = [(1,3),(5,2),(2,0),(4,5)]
sorted_data = sorted(data,key=lambda x:x[0])
print(sorted_data)