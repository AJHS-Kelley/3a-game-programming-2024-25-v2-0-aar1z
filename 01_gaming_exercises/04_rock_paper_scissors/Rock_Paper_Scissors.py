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
print(f"Hello{playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
if isCorrect == "yes":
    print(f"Ok {playerName}, let;s play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name and press enter.\n")