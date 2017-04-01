import sys

print "a" + sys.argv[1].title().replace(".", "").replace(" ", "_")