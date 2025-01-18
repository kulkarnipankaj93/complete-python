#Type casting- it is the conversion of an object from one data type to another data type.

#Implicit type conversion:
#Implicit type conversion is automatically performed by python interpreter.
#python avoids loss of data in implicit type conversion.
#for example:
l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
print(type(l3))  # here pyhton automatically converts l3 in to list

#Explicit type conversion:
#also called as type casting. data types of objects are converted using predefined functions by user
#loss of data may occur as we enforce objects to specific data type
#for example:
s4="123"
i1=int(s4)
print(i1)
print(type(i1))  #here we forcefully converts s4 into int

#Type casting functions
#int,oct,bin,hex,ord,chr,list,tuple