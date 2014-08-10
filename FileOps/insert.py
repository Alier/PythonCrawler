import re
import sys

def get_params(filename,seednum):
	pattern = '([0-9])*'+seednum
	f = open(filename,'r')
	matches = re.findall(pattern,f.read())
	f.close()
	params = []
	for match in matches:
		params += [match+seednum]
	return params
