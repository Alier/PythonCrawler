import re
import sys

#argv[1] is starting number, for example 317, if you want to add after 1317/2317/x317, etc for all eth link interfaces

#pattern = re.compile("[0-9]*"+str(317))
pattern = '([0-9])*'+sys.argv[1]
distance = 13

f = open('test.txt','r+')
matches = []
offset = 0
head_lines = []
new_lines = []
lineNum = 0

for line in f:
    match = re.findall(pattern,line)
#print match
    if (len(match)) :
        print match
        print type(match)
        head_lines += [lineNum]
        new_lines += [lineNum + distance]
        matches +=match
    lineNum += 1

print matches
print head_lines
print new_lines

# for each line , seek afterwards for the pattern of end of that section
patternEnd = "$ decimal places"
i = 0
for line in f:
    if i in new_lines:
        print i
        f.writeline("HELLO WORLD\n")
    else :
        continue

f.close()
#matches = re.findall(pattern,text)
#print matches
