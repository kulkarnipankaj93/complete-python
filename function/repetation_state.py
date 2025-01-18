#Repetation statement is used to repeat block of programming instructions like- for and while

#for loop- used to iterate over sequence either list,tuple,dictionary or set
#we can execute set of statements once for each item in list,tuple or dictionary.
#for example:
list1=[1,2,3,4,5]
for i in list1:
    print(i)

#while loop- used to execute block of statements repeatedly until given condition is satisfied.
#for example:
m=5
i=0
while i<=m:
    print(i)
    i+=1

#continue statement: it is used to skip the current iteration of the loop and control flow of program goes to next iteration
#for example- print odd numbers from 1 to 10 using continue statement
num=0
while num<10:
    num+=1
    if num%2==0:
        continue
    print(num)

#break statement:it is used to terminate the loop immediately when it is encountered
#for example: print numbers upto 3
for i in range(5):
    if i==4:
        break
    print(i)


#for-else & while-else: here we use else block after for and while loop
#else block gets executed after the completion of loop
#else block is not executed if we use break statment in the loop
#applications: used in searching program,to check the limits,to handle exceptions
#for example:
for i in range(5):
    print(i)
else:
    print("all numbers are printed")


#pass: it is null statement which can be used as placeholder for future code