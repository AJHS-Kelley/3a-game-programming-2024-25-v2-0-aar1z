# Awarding Extra Lives, Kristin Taylor v0.0

lives = 3
score = 10000
name = "kristin"

print(f"Hello {name}!  You scored {score} points.\n")

# Allows the user to input the score AS A INTEGER. <-- YOU ARE MISSING THIS PART OF THE CODE.  

# Output the score amd number of lives to the screen.

if score <= 10000:
   print("Lose a life")
   # Did not remove a life.  
elif score < 100001: # You put 10001 the first time.  Be careful about the values! 
   print("Give 1 extra life")
   lives += 1
elif score > 100000: # This block should be an else:  
   print("Give 2 extra Lives")
   lives += 2

print("lives: " + str(lives))
print("score: " + str(score))