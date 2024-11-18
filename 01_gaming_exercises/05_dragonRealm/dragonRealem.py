# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

#SAVING DATA TO FILE
# sTEPS 1 -- CREATE THE FILE NAME TO USE
logFileName = "dragonRealmLog.txt"
#logFileName = "dragonRealm.txt"
# Example: dragonRealmLog11:33am.txt

#step 2create the file
saveData = open(logFileName, "a")
#Files Modes
# x creates files, if file exist, exit with error message
# w creates files, if files exist, earase and overwrite 
# a creates files, if file exist append data to file

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now())+ "\n")

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
        
  
def chooseForest():
    pass

    
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
    choosePath = chooseCave()
    checkCave()
    if choosePath == 1
    print('Do you want to play again? (yes or no)')
    playAgain = input()

# Close the file
saveData.write("END OF GAME LOG\n\n")
saveData.save()