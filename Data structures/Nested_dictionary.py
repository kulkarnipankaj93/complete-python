# Nested Dictionary - Dictionary inside dictionary
class1={
    'student1':{
        'name':'pankaj',
        'age':30,
        'roll_num':1
    },
    'student2':{
        'name':'soni',
        'age':28,
        'roll_num':2


    }
}

class2={
    'student1':{
        'name':'Akshay',
        'age': 34,
        'roll_num': 1
    },
    'student2':{
        'name':'laxman',
        'age': 25,
        'roll_num':2
    }
}

# Printing nested Dictionary
print(class1)

# Accessing nested dictionary
print("Age of first student in first class is:", class1['student1']['age'])