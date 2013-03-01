# used rope refactoring to rename variables. (Not cheating, I guess)
# Additional string formatting characters available 
# http://docs.python.org/2/library/stdtypes.html#string-formatting

zed_name = 'Zed A. Shaw'
zed_age = 35  # not a lie
zed_height = 74  # inches
zed_weight = 180  # lbs
zed_eyes = 'Blue'
zed_teeth = 'White'
zed_hair = 'Brown'

print "Lets talk about %s." % zed_name
print "He is %s inches tall." % zed_height
print "He's %s pounds weight." % zed_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (zed_eyes, zed_hair)
print "His teeth are usually %s depending on the teeth" % zed_teeth

# This line is tricky try to get it exactly right
print "If I add %d, %d and %d I get %d" % (zed_age, zed_height, zed_weight, zed_age + zed_height + zed_weight)

# Printing with %r
print "If I add %r, %r and %r I get %r" % (zed_age, zed_height, zed_weight, zed_age + zed_height + zed_weight)
