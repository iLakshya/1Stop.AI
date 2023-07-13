# while loop basic example
counter = 56
while counter < 91:
    print(str(counter) + " - " + chr(counter))
    counter += 1       # this is the short way but it can also be written as: counter = counter + 1 but
print("end of the program")

# # using continue statement
# count = 56
# while count < 91:    # the program will not show anything as the count is not increasd before the continue statement
#     if count < 76:
#         continue
#     print(str(count) + " - " + chr(count))
#     count += 1
# print("end of the program")

count = 56
while count < 91:
    if count < 76:
        count += 1
        continue
    print(str(count) + " - " + chr(count))
    count += 1
print("end of the program")

# continue and break
count1 = 55
while count1 < 91:
    if count1 < 76:
        count1 += 1
        continue
    print(str(count1) + " - " + chr(count1))
    count1 += 1
    if count1 == 85:
        break
print("end of the program")

# example: print the odd numbers and if conuter reaches 100, break the loop
c = 0
while c < 100:
    if c % 2 == 0:
        c += 1
        continue
    print(c)
    c += 1
    if c == 100:
        break
print("end of the program")

# example: print the even numbers and if the counter reaches 100, break the loop
c = 0
while c < 100:
    if c %2 != 0:
        c += 1
        continue
    print(c)
    c += 1
    if c == 100:
        break
print("end of the program")