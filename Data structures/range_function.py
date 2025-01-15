# Range function and operations based on it
list1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = range(0,11)
# start: start value, if not provided it starts from 0.
# end/stop: sequence will end and this value will not be included in sequence. n-1.
# step: difference between each number in sequence. it is optional to provide. default=1
print(a)

tuple1 = tuple(range(10, 31, 2))
print(tuple1)

for i in tuple1:
    print(i)

# Immutable: elements can not be changed
# memory efficiency: generate sequence when the range function is used
for i in list1:
    if i == 3:
        print("True")

print(3 in range(0, 11))

print(tuple1[5])

