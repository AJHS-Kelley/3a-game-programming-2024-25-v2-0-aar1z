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

# MAIN GAME LOOP
loopCount = 0
loopsReq =int(input("How many loops do you want?\nEnter an integer, no commas, and press ENTER.\n"))
#req is the universal abbreviation in computer programing for REQUEST rews = request
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq:
    
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
    playerChoice = random.randint(0,2) # randomly select 0, 1, 2.
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
       numDraws += 1
    # draw
    elif playerChoice == "paper" and cpuChoice == "scissors":
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
        numDraws += 1
    # draw
    elif playerChoice == "scissors" and cpuChoice == "rock":
       print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
       cpuScore += 1 
    # cpu wins
    elif playerChoice == "scissors" and cpuChoice == "paper":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         playerScore += 1
    # player wins
    elif playerChoice == "scissors" and cpuChoice == "scissors":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         numDraws += 1    
    loopCount += 1
    #print the results to the screen
    #award point to the winner and output results
         
print(f" Your final score: {playerScore} AI final score: {cpuScore}.\nDraws: {numDraws}")
if playerScore > cpuScore:
    print(f"Congrats , you win!")
elif cpuScore > playerScore:
    print(f"The AI wins")
else:
    print("unable to determine a winner. \n please restart")
    exit()

rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of loops: {loopCount}\n")
print(f"Execution Time {rpsTime:.2F} seconds.\n")