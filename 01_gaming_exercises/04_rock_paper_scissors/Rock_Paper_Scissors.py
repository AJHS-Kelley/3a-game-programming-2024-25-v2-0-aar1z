# Rock paper scissors, Kristin Taylor v0.1

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore=0
playerName="Test Player"
playerChoice=None

# DATA STRUCTURES -- CPU
CPUscore=0
CPUscore=None

# PLAYER NAME INPUT
playerName = input("Type your name and press enter.\n")
print(f"Hello {playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

#.lower() turns all into lower case
#.upper() turns all into upper case

if isCorrect == "yes":
    print(f"Ok {playerName}, let;s play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name and press enter.\n")

#The RULES
print(f"""
Welcome {playerName} to the Rock, Paper, Scissors Robot
It's time to play Rock, Paper, Scissors!
      
You will be play against the CPU. The first player who scores 5 point wins.
You will choose either Rock, Paper and Scissor.
The CPU will also choose from Rock, Paper and Scissor at random.
      
1.ROCK BEATS SCISSORS
2.SCISSORS BEATS PAPER
3.PAPER BEATS ROCK
""")

# MULTI-LINE STRING CAN BE USED FOR BIG COMMENTS






# MAIN GAME LOOP
while playerScore < 5 and CPUscore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {CPUscore} points.\n")
    playerChoices = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoices != "rock" or playerChoice != "paper" or playerChoice != "scissors":
       playerChoices = input("Please enter rock, paper, or scissors and press enter.\n").lower() 
       if playerChoices != "rock" or playerChoice != "paper" or playerChoice != "scissors":
           print(" You are not following directions. Please try again.\n")
           exit()
       print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    #Let CPU slect choice at random
    #compare player choice to CPU choice
    #print the results to the screen
    #award point to the winner and output results