import re
import sys

ParamPrefix = "Param"
AssemPrefix = "Assem"
AssemExaPrefix = "AssemExa"

NameLine_EthlnkParam = "$ name"
EndLine_EthlnkParam = "$ decimal places"
EndLine_EthlnkAssem = ";"

EndLine_Param = "$ decimal places"
EndLine_Assem = ";"
EndLine_AssemExa = ";"

#get the first digits of last parameters, for example, last parameter for fa1/1 is 1317, then the seed for last parameter is 317, and we'll find all these parameters for all interfaces, would be 1,2,.... 16 maybe , which in turn maps to paramters 1317,2317,...16317, etc. To get the Line Paramxxxxx which we'll use later.

def get_first_digits(InputFile,LastParamSeed,Prefix):
	pattern = Prefix+'([0-9]*)'+LastParamSeed+' ='
	f = open(InputFile,'r')
	matches = re.findall(pattern,f.read())
	f.close()
	return matches


#from first digits and seed value, form the line of "	Param[paramNum]:" for later search purpose. returns a string
def get_SectionStartLine(firstDigit, ParamSeed, Prefix):
	return Prefix+firstDigit+ParamSeed+" ="

def get_allStartLines(firstDigitsList,ParamSeed,Prefix):
	allStartLines = []
	for digit in firstDigitsList:
		allStartLines += [get_SectionStartLine(digit,ParamSeed,Prefix)]
	return allStartLines


#from first parameter, get interface number, which would be just the hex of this first parameter. e.g : 1 -> 01, 10->0A, and 16->10
def get_intfNum(firstDigit):
	#print firstDigit
	val = hex(firstDigit).split('x')[1]
	if(firstDigit < 16):
		return ("0"+val).upper()
	else:
		return val.upper()

#return a string of the new section generated for ParamNum
def generate_section(sampleFile,ParamNum,intfNum,intfName):
	f = open(sampleFile,'r')
	newText =f.read()
	newText = newText.replace('[PARAMNUM]',ParamNum)
	newText = newText.replace('[INTFNUM]',intfNum)
	newText = newText.replace('[INTFNAME]',intfName)
	return newText

# return True if any substr in the subStrList can be found as part of curStr, otherwise return False
def substr_in_str(curStr,subStrList):
	for substr in subStrList:
		if curStr.find(substr) > 0 :
			return True

	return False

#inputs: 
#LastParamSeed:
#NewParamSeed:
#InputFile:EDS file to update
#SampleFile: sample feature section in file, with MACROS to be replaced
#output: Updated EDS file with name InputFile.eds_new

#!!!!this Routine would not work properly if the LastParam has been followed by an Enum section

def insert_ethlnk_param(InputFile, LastParamSeed, NewParamSeed, SampleFile):
	outputFile = InputFile+'_ethParam'
	firstDigitList = get_first_digits(InputFile,LastParamSeed,ParamPrefix)
	print firstDigitList
	startLines = get_allStartLines(firstDigitList,LastParamSeed,ParamPrefix)
	print startLines
	firstDigit = 0
	intfName = ''
	with open(InputFile,'r') as Input:
		with open(outputFile,'w') as Output:
			started = False
			for line in Input:
				Output.write(line)
				if substr_in_str(line,startLines) :
					started = True
					#print "START"
					firstDigit = line.split('m')[1].split(LastParamSeed)[0]
				if started and line.find(NameLine_EthlnkParam) > 0:
					intfName = line.split('"')[1].split(' ')[0]
				if started and line.find(EndLine_EthlnkParam) > 0:
					started = False
					#print "END"
					intfNum = get_intfNum(int(firstDigit))
					Param = firstDigit+NewParamSeed
					#print Param
					#print intfNum
					#print intfName
					newSection = generate_section(SampleFile,Param,intfNum,intfName)
					Output.write(newSection)
	Input.close()
	Output.close()

# for adding AssemX for each interface
def insert_ethlnk_assem(InputFile, LastAssemSeed, NewAssemSeed, SampleFile):
	outputFile = InputFile+'_ethAssem'
	firstDigitList = get_first_digits(InputFile,LastAssemSeed,AssemPrefix)
	print firstDigitList
	startLines = get_allStartLines(firstDigitList,LastAssemSeed,AssemPrefix)
	print startLines
	firstDigit = 0
	intfName = ''
	with open(InputFile,'r') as Input:
		with open(outputFile,'w') as Output:
			started = False
			lineNum = 0
			for line in Input:
				Output.write(line)
				if started :
					lineNum += 1
				if substr_in_str(line,startLines) :
					started = True
					#print "START"
					firstDigit = line.split('m')[1].split(LastAssemSeed)[0]
				if started and lineNum == 1 :
					#print line
					intfName = line.split('"')[1].split(' ')[0]
				if started and line.find(EndLine_EthlnkAssem) > 0:
					started = False
					#print "END"
					lineNum = 0
					intfNum = get_intfNum(int(firstDigit))
					assemNum = firstDigit+NewAssemSeed
					#print assemNum
					#print intfNum
					#print intfName
					newSection = generate_section(SampleFile,assemNum,intfNum,intfName)
					Output.write(newSection)
	Input.close()
	Output.close()
	
#insert static section from sectionFile into specific position in InputFile
#LastParamNum should be 31205 something like this
#Param is flag, if Param = True, then it's Paramxxxx feature ,otherwise, it's Assemxxxx feature

def insert_global_feature(InputFile, LastParamNum,sectionFile,Param):
	outputFile = " "
	startLine = " "
	endLine = " "
	if Param:
		outputFile = InputFile+'_param'
		startLine = "Param"+LastParamNum+" ="
		endLine = EndLine_Param
	else:
		outputFile = InputFile+'_assem'
		startLine = "Assem"+LastParamNum+" ="
		endLine = EndLine_Assem
	#print startLine
	with open(InputFile,'r') as Input:
		with open(outputFile,'w') as Output:
			started = False
			for line in Input:
				Output.write(line)
				#print line
				if line.find(startLine) > 0:
					started = True
					#print "START"
				if started and line.find(endLine) > 0:
					started = False
					#print "END"
					newSection = open(sectionFile,'r').read()
					#print newSection
					Output.write(newSection)
					#Output.write('\n')
	Input.close()
	Output.close()
