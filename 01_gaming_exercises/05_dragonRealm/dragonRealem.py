# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are in a land full of dangerous creatures')
    print('Your choices and luck will detrime if you can surive')
    time.sleep(2)
    print('In front of you there are two paths')
    print('One leading to a dark and deep forest')
    print('The other leading to two caves')
   
def choosepath():
    path = ''
    while path != '1' and path != '2':
        print('Which path do you choose? (1 or 2)')
        path = input()
    if path == 1:
        print("You have chosen the dark forest")
    elif path == 2:
        print("You have chosen the two caves")
        return path
  

    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    

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