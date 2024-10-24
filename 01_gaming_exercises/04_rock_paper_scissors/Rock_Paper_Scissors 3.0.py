# Rock paper scissors, Kristin Taylor v3.3

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerScore = 0
playerName ="Test Player"
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
def playerName()-> str: # Function signature -- name of
    """Gets the name from the player and returns it."""
    # The line above is a DOCSTRING, it gives a brief example of what the function does
    playerName = input("Type your name and press enter.\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

    if isCorrect == "yes":
       print(f"Ok {playerName}, let;s play Rock, Paper, Scissors!\n")
    else:
       playerName = input("Type your name and press enter.\n")
    return playerName

# CALLING THE FUNCTION
playerName = playerName()

#The RULES using MULTI-LINE STRING
def rules()-> None:
    """The function prints the rules for rock papaer, scissor"""
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
    # does another part of this program need to acess this information
    # if YES, you must have areturn statement
    # if NO, a return statement isn't require

def playerChoice()-> str:
 """Allows player to choose rock, paper, scissors"""
 while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
       playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower() 
       if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
           print(" You are not following directions. Please try again.\n")
           exit()
       print(f"You have chosen {playerChoice}.")
    else:
        print(f"You have chosen {playerChoice}.")
    return playerChoice
 
 def cpuChoice()-> str:
    """Allows the CPU to choose rock paper, scissors"""
    cpuChoice = random.randint(0,2) # randomly select 0, 1, 2.
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "scissors"
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("unable to detrimes CPU choice. \n Please restart")
        exit()
    print(f"AI Choice: {cpuChoice}")
    return cpuChoice
    
# Remove the lines of code that add score to player, CPU or draw below.
def pickWinner(playerChoice: str, cpuChoice: str) -> str:
    """Determines the winner using player and CPU choices."""
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
        print("The AI wins a point")
        cpuScore += 1
        return "CPU wins"
    elif playerChoice == "rock" and cpuChoice == "scissors":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         print("You win a point")
         playerScore += 1
         return "Player wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         print("It's a draw")
         return "Draw"
    if playerChoice == "paper" and cpuChoice == "scissors":
       print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
       print("The AI wins a point")
       cpuScore += 1
       return "CPU wins"
    elif playerChoice == "paper" and cpuChoice == "rock":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         ("You win a point")
         playerScore += 1
         return "Player wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         return "Draw"
    if playerChoice == "scissors" and cpuChoice == "rock":
       print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
       cpuScore += 1 
       return "CPU wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         playerScore += 1
         return "Player wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
         print(f" The AI chose {cpuChoice} and you chose {playerChoice}\n")
         print("It's a draw")
         return "Draw"
    else: 
         print("Unable to determine a winner. Please restart.\n")
         exit()

def score(winner: str) -> int:
    """This function uses the winner to update the score for CPU, Num. DRAWS, and player score."""
    if winner == "Player Wins":
       score = 1
    elif winner == "CPU Wins":
        score = 1
    else: # This is a DRAW. 
        score = 0
    return score

def playGame(playerScore: int, cpuScore: int) -> None:
    """This functio will use all other function to play rock, paper, scissor."""
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "Player win":
            playerScore += score(roundWinner)
        if roundWinner == "CPU win":
            cpuScore += score(roundWinner)

        print(f"Player Score; {playerScore}\n")
        print(f"CPU Score; {cpuScore}\n")

        if matchWinner(playerScore, cpuScore) == True:
           break

playGame(playerScore, cpuScore)

