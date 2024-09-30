# Rock paper scissors, Kristin Taylor v0.1

# MODULE IMPORTS
import random, time

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerChoice = None
numDraws = 0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# MULTI-LINE STRINGS CAN BE USED AS COMMENT 
# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    
    #Let CPU slect choice at random
    cpuChoice = random.randint(0,2) # randomly select 0, 1, 2.
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "scissors"
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("unable to detrimes AI choice. \n Please restart")
        exit()
    print(f"AI Choice: {cpuChoice}")
    #print(f"AI Choice: {cpuChoice}")
    cpuChoice = random.randint(0,2) # randomly select 0, 1, 2.
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "scissors"
    elif playerChoice == 2:
         playerChoice = "paper"
    else:
        print("unable to detrimes AI choice. \n Please restart")
        exit()
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
        print("The AI wins a point")
        cpuScore += 1
    # cpu wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         print("You win a point")
         playerScore += 1
    # player wins
    elif playerChoice == "rock" and cpuChoice == "rock":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         print("It's a draw")
    # draw
    if playerChoice == "paper" and cpuChoice == "scissors":
       print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
       print("The AI wins a point")
       cpuScore += 1
    # cpu wins
    elif playerChoice == "paper" and cpuChoice == "rock":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         ("You win a point")
         playerScore += 1
    # player wins
    elif playerChoice == "paper" and cpuChoice == "paper":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
    # draw
    if playerChoice == "scissors" and cpuChoice == "rock":
       print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
       cpuScore += 1 
    # cpu wins
    elif playerChoice == "scissors" and cpuChoice == "paper":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         playerScore += 1
    # player wins
    elif playerChoice == "scissors" and cpuChoice == "scissors":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
        
    
    #print the results to the screen
    #award point to the winner and output results
         
print(f" Your final score: {playerScore} AI final score: {cpuScore}.\n")
if playerScore > cpuScore:
    print(f"Congrats {playerName}, you win!")
elif cpuScore > playerScore:
    print(f"Th AI wins")
else:
    print("unable to determine a winner. \n please restart")
    exit()