# 01/26/2013

# Python will follow PEMDAS too
# P = paranthesis
# E = Exponents
# M = Multiplication
# D = Division
# A = Addition
# S = Substraction

print 'I will count the Hens'

print "Hens", 25 + 30/6  # 30
print "Roosters", 100 - 25 * 3 % 4
# 100 - 75 % 4
# 100 - 3
# 97

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - 1/4 + 6
# 6 - 5 - 0 + 6
# 7

print "Is that True 3 + 2 < 5 - 7 ?"

print 3 + 2 < 5 - 7

print "What is 3 + 2 ? ", 3 + 2
print "What is 5 - 7 ? ", 5 - 7

print "Oh, that is why it is False."

print "How about some more."

print "Is it greater ?", 5 > -2
print "Is it greater or equal ?", 5 >= -2
print "Is it less or equal ?", 5 <= -2
