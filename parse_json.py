import sys

# __author__ = 'chenliang'

with open(sys.argv[1], 'r') as f:
    print "------------------------------"
    read_data = f.read()
    print read_data
f.closed

