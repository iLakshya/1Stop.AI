# Lists
students = ["Mayank", 28, "Shashank", 98, "Vanshraj", 56]
# print(students)
# print(students[2])
for x in students:
    print(x)
for x in range(len(students)):
    print(x)
for x in range(0, len(students), 2):
    print(students[x], "Scored", students[x+1])
    
# to add any element in a list, we use append
students.append("Lakshya")
students.append(99)
print(students)

# to modify the list, just write the index value and then the new value which has to be modified
students[-1] = 90
print(students)

# adding two lists
students2 = ["Vedant", 89]
students.extend(students2)
print(students)

# removing the last 2 elements from the list
# students.remove[-2:]
students.remove("Vedant")
students.remove(89)
print(students)

print(students.count(44)) # counts how many times the number is present in the list

# pop function can also be used to remove the element
students.pop()     # by default last element is removed from the list
students.pop(-1)
print(students)

# remove all the elements from the list
# students.clear()
# print(students)

print(students.index(56))    # prints the index number of the element and if the number is not prresent, then it gives ValueError
print(students.index('Mayank'))

abc = ["Vanshraj", "Vedant", "Lakshya", "Manas", "Aaron", "Hiten"]
print(sorted(abc))
#OR
abc.sort(reverse=False)
print(abc)

# reverse the list
abc.reverse()
print(abc)
#OR
abc.sort(reverse=True)
print(abc)

# copy the elements of the list to another
abc1 = abc.copy()
print(abc1)

# using insert function
abc2 = abc.copy()
print(abc2)
abc2.insert(2, "Shubham")
print(abc2)