# Loops, Kristin Taylor, v0.0

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# while <-- Used when you dont know how many loops you'll need.

# for loops like Go Fish, you search each card for what the player asked.
# while loop is like musicals chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN interation.
# iterate through the list means use a for loop

# for loops Example -- Iterating a list
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    print(eachFruit)

# continue Keyword -- Skips the current iteration and the finishes the loop.
    fruits = ["apple", "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
     continue
    print(eachFruit)

# break Keyword -- Immediately exits the loop.
fruits = ["apple", "banana", "strawberry", "tomato"]
for eachFruit in fruits:
    if eachFruit == "banana":
     break
    print(eachFruit)

# for loops using range(). range(x) is EXCLUSIVE, it starts at 0 and ends at -1
for i in range(10): # range is 0 - 9
   print(i)
