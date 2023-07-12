# nested for loop (for loop inside another for loop)
mylist = ["First", "Second", "Third"]
for x in mylist:
    for y in range(10):
        print(y)
    print(x)
print("end of loop")

mylist1 = ["first", 30000, 'a']
for x in mylist1:
    for y in range(3):
        print(y)
    print(x)
print("end of loop")