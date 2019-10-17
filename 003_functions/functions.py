# Example file for working with functions

# define a basic function
def function1():
    print("I'm a function.")

# function that takes arguments
def function2(argument1, argument2):
    print(argument1, " ", argument2)

# function that returns a value
def cube(number):
    return number * number * number

# function with default value for an argument
def power(number, powerOf = 1):
    result = 1
    for loop_counter in range(powerOf):
        result = result * number
    return result

# function with variable number of arguments
def multi_add(*arguments):
    result = 0
    for number in arguments:
        result = result + number
    return result

function1()
print (function1())
print(function1)
function2("argument 1", "argument 2")
print(cube(3))
print(power(3))
print(power(3, 4))
print(power(powerOf = 4, number = 3))
print(multi_add(2, 15, 23, 9, 59, 38))