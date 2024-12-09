# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# You have basically done no work on this project Kristin.  
# I am concerned you will not finish, and you have not asked for help at all. 

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

numItem = 0
hasStake = False

while numItem < 1:
    itemsChosen = input("Taking a weapon is highly recommend on these adventures. Do you want to take one? (Yes/no):")
    if itemsChosen == 'yes':
        hasStake = True
        numItem += 1
    elif itemsChosen == 'no':
        hasStake = False
        numItem += 1
    else:
        print("You have to pick either Yes or No")
   

def displayIntro():

    print('You are in a land full of dangerous creatures')
    print('Your choices and luck will detrime if you can surive')
    time.sleep(2)
    print('In front of you there are two paths')
    print('One leading to a dark and deep forest')
    print('The other leading to two caves')
   
def choosePath():
    path = ''
    while path != '1' and path != '2':
        path = input('Which path do you choose? (1 or 2)')
    return # What are you returning here?  You need a variable, list, or expression to return a value. 
        
  
def chooseForest(hasStake: bool) -> bool:
    print('You walk into the dark forest')
    time.sleep(2)
    print('The tall trees cover any chance of sunlight shining through')
    time.sleep(2)
    print('You feel the tempertaure around you drop')
    time.sleep(2)
    print('You have the eerie feeling of being watched')
    time.sleep(4)
    print('Suddenly a pale creature with sharp teath charges at you')
    if hasStake == True:
        print('You quickly reacted to the pale creature')
        print('You charged the wooden stake toward the creature chest')
        print('The creature screams in pain as it flys away')
        print('You are alive')
    elif hasStake == False:
        print('The creature charges at you')
        print('You have nothing to defend yourself with')
        print('You feel the creature bite into your neck and suck your blood')
        print("You have died")
    



    
def chooseCave(chooseCave):
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    

def checkCave(chooseCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chooseCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chosenPath = choosePath()
    if chosenPath == '1':
        chooseForest()
    else:
        chooseCave()
    print('Do you want to play again? (yes or no)')
    playAgain = input()

# Close the file
saveData.write("END OF GAME LOG\n\n")
saveData.save()

# Code crashes immediately after trying to choose a cave, no matter if I select 1 or 2. 