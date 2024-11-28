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
myNumber = int(input("Please type an INTEGER number and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
# int() will convert the data to an integer if possible.
newNumber = input("Please type a value and press enter.\n")
print(int(newNumber)) # can convert SRING to INTGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can covert INTGER to STRING.

# float() will convert the data to a float if possible.
newNumber = input("Please type a value and press enter.\n")
#print(int(newNumber)) <-- cannot covert FLOAT to INTGER.
print(float(newNumber)) # can convert STRING to FLOAT
print(str(newNumber)) # can convert FLOAT to STRING

# str() will convert the data to a string if possible.
myNumber = 5
print(newNumber + newNumber) # Should print 10
print(str(newNumber + newNumber)) # Should print 55