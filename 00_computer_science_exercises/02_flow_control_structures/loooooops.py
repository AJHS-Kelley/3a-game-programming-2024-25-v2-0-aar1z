# Loops, Kristin Taylor, v0.0
import random # import the random module for us to use.
# Generally put all your import statement at the top.

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# while <-- Used when you dont know how many loops you'll need.

# for loops like Go Fish, you search each card for what the player asked.
# while loop is like musicals chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN interation.
# iterate through the list means use a for loop

# for loops Example -- Iterating a list
#fruits = ["apple", "banana", "strawberry", "tomato"]
#for eachFruit in fruits:
    #print(eachFruit)

# continue Keyword -- Skips the current iteration and the finishes the loop.
    #fruits = ["apple", "banana", "strawberry", "tomato"]
#for eachFruit in fruits:
    #if eachFruit == "banana":
     #continue
    #print(eachFruit)

# break Keyword -- Immediately exits the loop.
#fruits = ["apple", "banana", "strawberry", "tomato"]
#for eachFruit in fruits:
    #if eachFruit == "banana":
     #break
    #print(eachFruit)

# for loops using range(). range(x) is EXCLUSIVE, it starts at 0 and ends at -1
for i in range(10): # range is 0 - 9
   print(i)

# Might not always want to start at 0.
for i in range(10, 100): #
   print(i)

# Not want to count by 1
for i in range( 10, 100, 5): # 10 = start, 100 - 1 = stop, 5 = # to count by.
   print(i)

# Sometimes you're not done writing loops.
for x in range(10):
   pass # tells Pythons this loops isn't finished, dont freak out.

# while loops -- Musical chairs
playerScore = 0
counter = 0
while playerScore < 100: # Run as long as this is True.
   print(f"Starting: {playerScore}")
   playerScore += random.randint(1,100)
   print(f"After: {playerScore}")
   counter += 1
print(f"counter: {counter}")