# Explains different types of string formattings
student1 = "Pankaj"
roll_number = 5
grade = 'A'
standard = 10

# f strings- Arguments are provided with in {} while declaring string
str1 = f"Name of the student is {student1}. Roll number is {roll_number}."
print(str1)


# str.format- Arguments are provided inside format function
#          - one to one mapping is done for the arguments
#          - If we provide less number of arguments than required it gives 'IndexError'
#          - If we provide more number of arguments than required it simply ignore the extra
str2 = "Name of student with grade {} and roll number {} is {}.".format(grade,roll_number,student1)
print(str2)


# str.format - with index - We provide index values for the arguments in the sequence it is to be used
#          - If we forgot to provide any index value it provides 'ValueError'
str3 = "A student with name {2} and grade {0} has roll number {1}".format(grade,roll_number,student1)
print(str3)

# Old style formatting using % operator - We use % sign and specify the data type which is to be used
#                                     - If we provide less number of arguments than required it gives 'TypeError'
str4 = "Standard %d student with name %s has roll number %d" % (standard, student1, roll_number)
print(str4)

