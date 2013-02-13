# Define cheese_and_crackers function
def cheese_and_crackers(cheese_count, boxes_of_crakers):
    # print cheese count 
    print "You have %d cheeses!" % cheese_count
    # print cracker count
    print "You have %d boxes of crackers" % boxes_of_crakers
    # Idea of a party
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Passing numbers directly in to the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Define variables with cheese count and crackers count
print "Or, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# passing variables into the function defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Do math (addition) while passing arguments into the
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Combine both variables and number and do the math. Oh, it is already printed below.
print "And we can combine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
