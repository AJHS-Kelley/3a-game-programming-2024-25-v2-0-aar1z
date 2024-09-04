# Flow Control Structures, Kristin Taylor, v0.0
# Making Computer Program Make Decisions

temperature = 99.35
color = "Blue"
height = 5
likesPineappleOnPizza = True

# SINGLE DECISION POINT - if Statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISION OPERATOR 99% of the time
    # runThisCode IF THE CONDITIONAL_EXPRESSION is True

if temperature > 100:
   print("Bring a hat and water.\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if likesPineappleOnPizza:
  print("Yummy")

  # What if we want something different to happen?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USUNG = instead of ==
     print("Your shirt is the correct uniform color.\n")
else:
   print ("Your shirt is not the correct uniform color.\n")

pathAhead= "Rainy"
if pathAhead == "Clear":
   keepDriving = True
else:
   keepDriving = False

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# MUST BE > min. height and < max. height to ride
   
if height >= 3:
   print("You're tall enough to ride the Tea Cups!\n")
elif height >= 6:
 print("You're too tall to ride the Tea Cups!\n")
else: # "oh, no, something's wrong!"
   print("Error, height not dectected. Do not ride!\n")


# When writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >=
# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3:
   print("You're not tall enough to ride the Tea Cups!\n")
elif height < 6:
 print("You're tall enough to ride the Tea Cups!\n")
else: # "oh, no, something's wrong!"
   print("Error, height not dectected. Do not ride!\n")

if temperature >= 100:
   print("print it's too hot, no recess.\n")
elif temperature >= 50:
   print("Recess is allowed for today.\n")
elif temperature > 0:
   print("Recess will be in the gym.\n")
else:
   print("Error, Temp not dected. no recess\n")