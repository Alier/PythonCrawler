import sys

pattern = "param"+sys.argv[1]
f = open('lines.txt','r')
for line in f:
	print line
	if line.startswith(pattern):
		print "STARTWITH TRUE"
	elif line.find(pattern) > 0:
		print "FIND true"
	elif line.endswith(pattern):
		print "END true"
	else:
		print "Wrong Line"
