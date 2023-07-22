# functions
def func1():        # basic function
    print("Hello")
func1()      # calling the function

def func2(name):       # pass any variable to the function parameter
    print("Hi there", name)
func2('Lakshya')   # passing value in the function parameter

def func3(name="Mayank"):
    print("Hi there", name)
func3()           # calling the function without passing any value in the parameter (default value)
func3("LL")       # we can also change the value based on calling the function

# multiple parameters can be passed inside the function
def func4(name = "Lakshya", repeat = 2):
    for i in range(repeat):
        print(name)
func4()
func4.__doc__

# return statement
def sqr_number(x):
    return x**2
print(sqr_number(2))