# Data Types and Operators, Kristin Taylor. v0.0

# Fundamentals Data Types
#string- str- Sequence of letters, number and spaces
#Strings in Python are insie ' " or " "

# Boolean- bool- True or false values.

# Float - float- any number value with a decimal,+\- including 0

# Intergers- int- any whole number, +\- including 0

# Data types are stored in variables.
#VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED
#VARIABLE CANNOT START WITH A NUMBER
#camelCaseVariableNnames
#snake_case_variable_names

# DECLARING VARIABLE AND ASSIGNING VAULES

high_score=223 # int data types

carSpeed = 16.23 #int data types

hasAxe = True # boolean data types
isPurple = False # boolean data types

playerName = "Kristin Taylor" # string data types
enemyType = "fire" # string date type

# ASSIGN NEW VALUES
playerName 
carSpeed=1.25

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 5.0

# Printing Data types
newInt = 3
newFloat = 4.0
newString = "Skibidi Toilet"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

#printing Variables to Console / Screen
# print(playerName)
# print(isPurple)
# print(high_score)
# print(carSpeed)

# printing variable and epressions to console / screen
# print (high_score + 5000)
# print(4 * 12)
# print(high_score)


# PRINTING VARIABLES INSIDES OF STRINGS
# print(f"Hello{playerName}. Good job your high score is {high_score}. \n")

#ARITHIMATIC OPERATIONS
myInt = 69
myFloat = 2.57

# addition
myInt = 7 + 10
myFloat = 2.0 + 3.25

myInt = myInt + 5

myNum = myInt + myFloat

# When you add a int and a float together, the answer becomes a float

#subtraction
MyNum = myInt - myFloat
myInt = myFloat - 1.25

#Mulitplication 
myNum = myInt * myFloat

#Division
myNumber = myInt / myFloat # first is numerator, second num is denominator

# MODULES (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULES IS DETERMING EVEN / ODD NUMBER.
numStudents = 6
numSlicesPizza = 35

leftOvers = numSlicesPizza % numStudents
print(leftOvers)

# EXPONETS **
NUMsQUARED = 5 ** 2 # 5 is the base, 2 is the exponets.

# FLOOR-DIVISION // --, throws out any decimals
myNum = myInt // myFloat

# Addition-Assignment Operator - Mostly used for counters.
myNum= 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness

# COMPARISON OPERATIOR

# IS-EQUAL-TO == Are the two vaules equal to each other?
# Returns True or False based on evaluation.
x = 5
# print(x == 5)

# NOT-EQUAL-TO != Are the two values NOT equal?
# Returns True or False based on evaluation.
# print(x != 12)

# # GREATER THAN / GREATER-THAN-OR-EUAL-TO
# print(5 > 3) # LESS than
# print(12 <= 2) # Less than or Equal to

# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 44
height = 73.5
eyeColor = "brown"
# In order to ride the teacups, you must be at least 18 years old and 60".
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Pink")
# ALWAYS CHECKS FOR THE LEST-LIKELY TO BE FALSE CONDITION FIRST!!!!!
#print(defeatedBoss == True and level > 5 and hasBlueKey == True)

# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATMENT TO BE TRUE
# print(age >= 18 and height >= 60)
# print(age >= 18 and height >= 60 and eyeColor == "Pink")
# ALWAYS CHECKS FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
# print(defeatedBoss == True or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPSITE VALUE OF THE STATMENT.
a = 5
print( a == 5)
print(not (not (a == 5)))

# COMBINING LOGICAL OPERATORS
#print(a == 5 and hasKey == True or isCloud == True)

# IDENTIY OPERATORS
g =1.0
h =1.0
i = g
print(g is h)
print(i is h)
print( i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = [ "apple", "banana," "tomato"]
print("banana" in fruits)
print("potato" in fruits)

