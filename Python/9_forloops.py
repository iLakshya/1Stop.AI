# loop will work from 0 to 9, (n-1)
for x in range(10):
    print("Iteration Number", x)
print("Outside for loop")

# if some specific starting and ending has to be given then we can use , in the range function
for x in range(2,10):
    print("Iteration Number", x)
print("for loop ends")

# if we want to skip some numbers then add another comma after range
for x in range(2,10,2):        # loop will work with a gap of 2
    print("Iteration Number", x)
print("for loop ends")

# looping using strings
my_str = "Lakshya"
for x in my_str:
    print(x)
print("End of the loop")

# looping using lists
my_list = [1, "a", "A", 0.12, "End of the list"]
for x in my_list:
    print(x)
print("End of the loop")