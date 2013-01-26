# Assign varialbe with 10 types of pepole
x = "There are %s types of people" % 10

# Define binary, and non binary variables
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

# Print strings about 10 types of people
print x
print y

# Pring strings with "" and ''
print "I said: %r" % y
print "I also said: '%s'" % y

# Including boolean in a string
hilarious = False
joke_evaluation = "Isn't that joke so funny ?! %r"

print joke_evaluation % hilarious

# String concatination using +
e = "This is the left side of..."
w = "a string with a right side"

print e + w
