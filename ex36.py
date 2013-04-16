"""
Dinesh Weerapurage
04/02/2013
Home work game
"""
import sys

# Entrance
def main_etntrance():
    print "You are a mouse. Now you are entering into a big warehouse which smells cheese"
    print "Input 1 to go forward, 0 to exit"
    ui = int(raw_input("> "))
    if ui > 0:
        print "Moving fowrad"
        return 1
    return 0

def onthe_hallway():
    print "Now you are on a hallway, there are two rooms"
    print "Input\n 1. Goto room on the left \n 2. Goto room on the right \n 3. Search for cheese \n 0. exit"
    return int(raw_input("> "))

def left_room():
    print "Now you are in Room 1"
    print "Input\n 1. Go back \n 2. Search for cheese \n 0. exit"
    return int(raw_input("> "))

def right_room():
    print "Now you are in Room 2"
    print "Input\n 1. Go back \n 2. Search for cheese \n 0. exit"
    return int(raw_input("> "))        
    
# command line for the game.
status = 0
i = 0
while(1):
    if status == 0:
        status = 1
        i = main_etntrance()

    # Two if condtions to navigate on hallway and rooms
    if i == 0:
        sys.exit(0)
    elif status == 1:
        status = 2
        i = onthe_hallway()

    if i == 0:
        sys.exit(0)
    elif i == 1 and status == 2:
        status = 3
        i = left_room()
    elif i == 2 and status == 2:
        status = 4
        i = right_room()
        
    # if else condition to search for cheese
    if i == 0:
        sys.exit(0)
    elif (status == 3 or status == 4) and i == 1:
        # send to hallway
        status = 1
        continue
    elif status == 2 and i == 3:
        status = 1
        print "No Cheese on the hall way"
    elif status == 3 and i == 2:
        status = 1
        print "No Cheese in Room 1"
    elif status == 4 and i == 2:
        status = 1
        print "You found it !!"
    else:
        print "A monster going to eat you!! Run"
        sys.exit(0)
