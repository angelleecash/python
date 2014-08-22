__author__ = 'chenliang'

total = 0.0
logfile = open('/Users/chenliang/tmp/logs/access.log')

# for line in logfile:
#     # print line
#
#     size = int(line.split(" ")[9]);
#     total += size
#     print size

# print str(total/1024/1024) + " M"

bytecolumn = (line.split(" ")[9] for line in logfile)
bytes = (int(x) for x in bytecolumn)

print "Total:", sum(bytes)
