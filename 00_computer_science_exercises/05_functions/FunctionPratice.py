# Function Pratice, Kristin Taylor, V0.0

import random

#def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose. """ # DOCSTRING
    # print a list of languages to the screen, at least three but no more ghan five.
    # allow the user to select (input) a choice for the language.
    # print " Hellow, World!" to the screen in that language
    print("""
        Hello user, Choose one of the following languages 
        The following languages are avaiable
          [E]nglish
          [S]painsh
          [J]apanese
          [F]rench
          [G]erman
          """).lower() 
   
          
    language = input("What language do you want?\n").lower() 
    if language == "S":
        print("Hola Mundo")
    
    elif language == "E":
        print("Hello World")
    
    elif language == "J":
        print("Kon'nichiwa sekai")
    
    elif language == "F":
        print("Bonjour le monde")
    
    else: 
        print("Hallo Welt")

helloWorldMulti() # Function

# Function to Deterime Even / Odd Numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1: int) -> bool: # Requires one aggument (agrument1) and Returns a Boolean value.
    """Determines if an integer value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False
print(isEven(argument1))

# Function with Mulitple Arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("You can ride.\n")
    else:
        print("You cannot ride.\n")

canRideRollerCoaster(4, 10) # Arguments must be passed in the same order as the function sognature indicates.
