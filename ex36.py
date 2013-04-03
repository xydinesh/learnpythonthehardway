"""
Dinesh Weerapurage
04/02/2013
Home work game
"""

# command line for the game.
while(1):
    ui = raw_input("> ")
    if ui == "Exit" or ui == "exit":
        break
    else:
        print "You said '%s'" % ui
