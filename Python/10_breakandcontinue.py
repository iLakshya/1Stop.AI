# break statement
for x in range(20):
    print(x)
    if x == 10:
        break
print("End of the loop")

# 'a' is checked
for x in "Lakshya":
    print(x)
    if x == 'a':
        break
print("End of the loop")

# 'A' is checked
for x in "Lakshya":
    print(x)
    if x == 'A':
        break
print("End of the loop")

# continue statement
for x in range(20):
    print(x)          # print statement is used before if loop, hence 10 will be printed
    if x == 10:
        continue
print("End of the loop")

for x in range(20):
    if x == 10:
        continue
    print(x)          # print statement is used after if loop, hence 10 won't be printed
print("End of the loop")

# string manipulation
for x in "Lakshya":
    if x == 'a':
        continue
    print(x)
print("End of the loop")

for x in "Lakshya":
    if x == "A":
        continue
    print(x)
print("End of the loop")