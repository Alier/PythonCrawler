import re
import sys

def get_first_num_of_params(filename,seednum):
	pattern = '([0-9]*)'+seednum
	f = open(filename,'r')
	matches = re.findall(pattern,f.read())
	f.close()
	return matches
