i = 0
numbers = []
n = int(raw_input("Input a number > "))
inc = int(raw_input("Input increment > "))

while i < n:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + inc
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

# Write with a forloop
i = 0
numbers = []
print "Write with a for loop"
for i in xrange(0,n, inc):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    

for num in numbers:
    print num
