start = "\tParam1317"
end = "\tend"
to_insert = open('to_insert.txt','r').read()

with open('orig_file.txt','r') as inputFile:
	with open('new_file.txt','w') as outputFile:
		started = False
		for line in inputFile:
			outputFile.write(line)
			if line.startswith(start):
				print "START section"
				started = True
			if started and line.startswith(end):
				print "End of section"
				started = False
				outputFile.write(to_insert)
