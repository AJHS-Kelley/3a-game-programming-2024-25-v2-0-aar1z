# Awarding Extra Lives, Kristin Taylor v0.0

lives = 3
score = 10000
name = "kristin"

print(f"Hello {name}!  You scored {score} points.\n")

# Allows the user to input the score AS A INTEGER.

# Output the score amd number of lives to the screen.

if score <= 10000:
   print("Lose a life")
elif score < 10001: 
   print("Give 1 extra life")
   lives += 1
elif score > 100000:
   print("Give 2 extra Lives")
   lives += 2

print("lives: " + str(lives))
print("score: " + str(score))