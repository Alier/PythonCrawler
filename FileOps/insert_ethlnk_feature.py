import re
import sys

NameLineComment = "$ name"
EndLineComment = "$ decimal places"

#get the first digits of last parameters, for example, last parameter for fa1/1 is 1317, then the seed for last parameter is 317, and we'll find all these parameters for all interfaces, would be 1,2,.... 16 maybe , which in turn maps to paramters 1317,2317,...16317, etc. To get the Line Paramxxxxx which we'll use later.

def get_first_digits(InputFile,LastParamSeed):
	pattern = '([0-9]*)'+LastParamSeed
	f = open(InputFile,'r')
	matches = re.findall(pattern,f.read())
	f.close()
	return matches


#from first digits and seed value, form the line of "	Param[paramNum]:" for later search purpose. returns a string
def get_SectionStartLine(firstDigit, ParamSeed):
	return "\tParam"+firstDigit+ParamSeed+":\n"

def get_allStartLines(firstDigitsList,ParamSeed):
	allStartLines = []
	for digit in firstDigitsList:
		allStartLines += [get_SectionStartLine(digit,ParamSeed)]
	return allStartLines


#from first parameter, get interface number, which would be just the hex of this first parameter. e.g : 1 -> 01, 10->0A, and 16->10
def get_intfNum(firstDigit):
	print firstDigit
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

#return a string of the new section generated for ParamNum
def generate_section(sampleFile,ParamNum,intfNum,intfName):
	f = open(sampleFile,'r')
	newText =f.read()
	newText = newText.replace('[PARAMNUM]',ParamNum)
	newText = newText.replace('[INTFNUM]',intfNum)
	newText = newText.replace('[INTFNAME]',intfName)
	return newText

#inputs: 
#LastParamSeed:
#NewParamSeed:
#InputFile:EDS file to update
#SampleFile: sample feature section in file, with MACROS to be replaced
#output: Updated EDS file with name InputFile.eds_new

def insert_ethlnk_feature(InputFile, LastParamSeed, NewParamSeed, SampleFile):
	outputFile = InputFile+'_new'
	firstDigitList = get_first_digits(InputFile,LastParamSeed)
	print firstDigitList
	#digit_to_intfName_Map = get_firstDigit_intfName_mapping(InputFile,firstDigitList,LastParamSeed)
	#print digit_to_intfName_Map
	startLines = get_allStartLines(firstDigitList,LastParamSeed)
	print startLines
	firstDigit = 0
	intfName = ''
	with open(InputFile,'r') as Input:
		with open(outputFile,'w') as Output:
			started = False
			for line in Input:
				Output.write(line)
				if line in startLines:
					started = True
					firstDigit = line.split('m')[1].split(LastParamSeed)[0]
				if started and line.find(NameLineComment) > 0:
					intfName = line.split(' ')[0].split('"')[1]
				if started and line.find(EndLineComment) > 0:
					started = False
					intfNum = get_intfNum(int(firstDigit))
					Param = firstDigit+NewParamSeed
					newSection = generate_section(SampleFile,Param,intfNum,intfName)
					Output.write(newSection)
					#Output.write('\n')
	Input.close()
	Output.close()
