from sys import argv
script, input_file = argv

# Read content of a file
def print_all(f):
    print f.read()

# Reset the file pointer of file, Oh, I forgot this is python not C
def rewind(f):
    f.seek(0)

# Print a line
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open current file named "input_file" to read
current_file = open(input_file)

print "first let's print the whole file:\n"

# Print everything form the input file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Rewind the file
rewind(current_file)

print "Let's print three liness:"

# Printing line by line
current_line = 1
print_a_line(current_line, current_file)

# Change source code to use += notation
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
             
                    
