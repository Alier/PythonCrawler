import find_pattern
import sys

def get_intfNum(firstDigit):
	val = hex(firstDigit).split('x')[1]
	if(firstDigit < 16):
		return ("0"+val).upper()
	else:
		return val.upper()

#get mapping from firstDigitList to interface names. As different SKUs might have different mapping, we just use the orig file to get the mapping without analyzing the SKUs. return a dictionary of {firstDigit1:intfname1, firstDigit2:intfname2,....}

def get_firstDigit_intfName_mapping(InputFile,firstDigitsList,LastParamSeed):
	mapping = {}
	with open(InputFile,'r') as inputFile:
		started = False
		key = None
		startLines = get_allStartLines(firstDigitsList,LastParamSeed)
		for line in inputFile:
			if line in startLines:
				started = True
				key = line.split('m')[1].split(LastParamSeed)[0]
			if started and line.find(NameLineComment) > 0:
				started = False
				value = line.split(' ')[0].split('"')[1]
				mapping[key]=value
	inputFile.close()
	return mapping


#argv[1] is starting number, for example 317, if you want to add after 1317/2317/x317, etc for all eth link interfaces

orig_filename = sys.argv[1]
seed_num = 317
to_add_num = 319
laterPartOfParam = str(seed_num)
newLaterPartOfParam = str(to_add_num)

#get the string format of first digit of all related params following with seed_num
first_params = find_pattern.get_first_num_of_params(orig_filename,laterPartOfParam)

#print first_params
intfNums = []
intfNames = []
Params = {}

for param in first_params:
	first_digit = int(param)
	intfNums += [get_intfNum(first_digit)]
	Params["\tParam"+param+laterPartOfParam+":\n"]= "["+param+newLaterPartOfParam+"]\n"

print Params
print intfNums

start = "\tParam"
end = "\tend"
#content_file = open('to_insert.txt','r')
#to_insert = content_file.read()


with open('orig_file.txt','r') as inputFile:
	with open('new_file.txt','w') as outputFile:
		started = False
		for line in inputFile:
			outputFile.write(line)
			if line in Params.keys():
				print "START section"
				started = True
				key = line
				print key
			if started and line.find("$ name") > 0:
				intfNames += [line.split(' ')[0].split('"')[1]]
			if started and line.startswith(end):
				print "End of section"
				started = False
				outputFile.write(Params.get(key))
				#outputFile.write(intfName)
inputFile.close()
outputFile.close()
print first_params
print Params
print intfNums
print intfNames
