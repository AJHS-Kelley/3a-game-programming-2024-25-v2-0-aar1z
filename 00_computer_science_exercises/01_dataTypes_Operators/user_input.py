# USER INPUT PRATICE, KRISTIN TAYLOR, V0.0

# input() is the bulit-in function to get information from the KEYBOARD.
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter.\n")
print(variableName)

# input() save ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() save ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() save ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!
# input() save ALL INPUT TO STRING DATA TYPES BY DEFAULT!!!

# INCOORECT, CAUSES A CONCATENATION
#myNumber = input("Please type an INTEGER number and press enter.\n")
#print(myNumber + 5)

# CORRECT -- Use a wrapper.
myNumber = input("Please type an INTEGER number and press enter.\n")
print(myNumber + 5)

# Wrapper Functions
# int() will convert the data to an integer if possible.
# float() will convert the data to a float if possible.
# str() will convert the data to a string if possible.