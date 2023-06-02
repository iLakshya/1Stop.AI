# Concatenation
des = "Sir"
fname = 'Ratan'
lname = 'Tata'
fullname = des + fname + lname
print(fullname)
print(len(fullname))
fullnamespaces = des + " " + fname + " " + lname
print(fullnamespaces)
print(len(fullnamespaces))

# Checks whether the alphabet is present or not in the string or not
# In Python "" and '' is the same thing which is used for the string
print('Ratan' in fullname)
print('Ratan' not in fullname)
print("a" in fullname)
print("a" not in fullname)
print("s" in fullname)
print("s" not in fullname)
print(" " in fullname)
print(" " in fullnamespaces)

# Individual Charactrs with the position
print(fullname[:])
print(fullnamespaces[:])
print(fullname[0])
print(fullname[1])
print(fullnamespaces[4])
print(fullnamespaces[3])       # checks the character from the front
print(fullnamespaces[-4])      # checks the character from backwords
print(min(fullname))
print(max(fullname))
print(min(fullnamespaces))
print(max(fullnamespaces))

# Some more functions
print(fullname.capitalize())
print(fullname.lower())
print(fullname.upper())
print(fullname.title())

a = "Hello world I am lakshyaGoel"
print(a)
print(a.capitalize())
print(a.lower())
print(a.upper())
print(a.title())
print(a.swapcase())