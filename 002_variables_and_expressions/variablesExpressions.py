# Variables and expressions

# Declare a variable and initialize it
variable = 0
print(variable)

# re-declaring the variable works
variable = "global variable"
print(variable)

# ERROR: variables of different types cannot be combined
print("This is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
    global variable
    variable = "new global variable"
    print(variable)

someFunction()
print(variable)

# deletes variable Raises ERROR variable not defined.
del variable
print(variable)