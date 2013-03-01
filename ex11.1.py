# comma ',' at the end of line is important
# as it allow you to enter answer next to the question
# i.e. it won't insert a \n at the end of the line
print "What is your eye color?",
eye_color = raw_input()
print "What is your hair color?",
hair_color = raw_input()
print "Enter a number you can think of",
n1 = int(raw_input())
print "Enter another number",
n2 = int(raw_input())

print "You have %s eys, %s hair and sum of numbers you entered %d" %\
(eye_color, hair_color, n1 + n2)
