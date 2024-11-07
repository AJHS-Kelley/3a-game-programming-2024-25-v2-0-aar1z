# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
playerChoice = None

def displayIntro():

    print('You are in a land full of dangerous creatures.')
    print('In front of you, you see two paths')
    print('One leads to a dark and deep forest the other leads to a dangerous cave')
    playerChoice = input("Enter your choice (1 or 2): ")

if playerChoice == "1":
    print("You chose the dark Forest.")

elif playerChoice == "2":
    print("You chose the dangerous cave.")
def chooseForest():
    hasBlade = False
    

    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()