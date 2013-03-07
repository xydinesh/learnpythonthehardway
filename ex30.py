people = 100
cars = 40
buses = 15

# cars are greater than people
if cars > people:
    print "We should take the cars."
# more people than cars
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

# more buses than cars
if buses > cars:
    print "That's too many buses."
# more cars than buses
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

# more people than buses
if people > buses:
    print "Alright, lets just take the buses."
else:
    print "Fine, let's stay home then."
