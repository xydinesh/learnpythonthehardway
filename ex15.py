# import argv from sys
from sys import argv

# unpack first two arguments into variable script and filename
# note: we have to provide filename as an argument
script, filename = argv

# open file given in 'filename'
txt = open(filename)

# print out filename
print "Here's your file %r:" % filename

# read content of the file
print txt.read()

# close file descriptor
txt.close()
# Asking user to type filename again
print "Type the filename again:"
file_again = raw_input("> ")

# open file for second type
txt_again = open(file_again)

# print the content of the file
print txt_again.read()

#close file descriptor
txt_again.close()
