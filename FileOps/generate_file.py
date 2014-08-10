
def generate_new_feature_section(ParamNum,INTFNUM,INTFNAME):
	print str(ParamNum) + " " + INTFNUM + " "+INTFNAME + "\n"
	with open('file_sample.txt','r') as sampleFile:
		with open('generated_file.txt','w') as outputFile:
			for line in sampleFile:
				if line.find('[PARAMNUM]') > 0 :
					newline = line.replace('[PARAMNUM]',str(ParamNum))
				elif line.find('[INTFNUM]') > 0:
					newline = line.replace('[INTFNUM]',INTFNUM)
				elif line.find('[INTFNAME]') > 0:
					newline = line.replace('[INTFNAME]',INTFNAME)
				else :
					newline = line
				print newline
				outputFile.write(newline)

generate_new_file(1317,"01",'Fa1/1')
